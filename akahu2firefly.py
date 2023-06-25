from json import loads, dumps
import re
import requests
import sqlite3
from dateutil import parser
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
from db_manager import db_manager

import firefly_iii_client

from firefly_iii_client.api import accounts_api
from firefly_iii_client.api import transactions_api
from firefly_iii_client.model.account_array import AccountArray
from firefly_iii_client.model.account import Account
from firefly_iii_client.model.account_read import AccountRead
from firefly_iii_client.model.account_single import AccountSingle
from firefly_iii_client.model.account_store import AccountStore
from firefly_iii_client.model.account_update import AccountUpdate
from firefly_iii_client.model.short_account_type_property import (
    ShortAccountTypeProperty,
)
from firefly_iii_client.model.account_role_property import AccountRoleProperty
from firefly_iii_client.model.transaction_store import TransactionStore
from firefly_iii_client.model.transaction_split_store import TransactionSplitStore
from firefly_iii_client.model.transaction_type_property import TransactionTypeProperty
from firefly_iii_client.model.transaction_read import TransactionRead
from firefly_iii_client.model.transaction_single import TransactionSingle


class akahu2firefly:
    @staticmethod
    def get_akahu_headers():
        akahu_headers = {
            "Accept": "application/json",
            "X-Akahu-Id": os.getenv("AKAHU_APP_CLIENTID"),
            "Authorization": "Bearer " + os.getenv("AKAHU_TOKEN"),
        }
        return akahu_headers

    def main(self):
        load_dotenv()
        self.firefly_accounts_by_account_id: dict[str, dict] = {}
        self.firefly_accounts_by_number: dict[str, dict] = {}
        self.akahu_accounts_by_account_id: dict[str, dict] = {}
        self.akahu2firefly = {}
        self.firefly2akahu = {}

        self.handled_akahu_transaction_types = [
            "TRANSFER",
            "DEBIT",
            "DIRECT DEBIT",
            "EFTPOS",
            "TAX",
            "INTEREST",
            "FEE",
            "CREDIT",
        ]
        self.firefly_transaction_type_from_akahu_type = {
            "TRANSFER": "transfer",
            "DEBIT": "withdrawal",
            "EFTPOS": "withdrawal",
            "DIRECT DEBIT": "withdrawal",
            "PAYMENT": "withdrawal",
            "TAX": "withdrawal",
            "INTEREST": "deposit",
            "FEE": "withdrawal",
            "CREDIT": "deposit",
        }

        # Configure OAuth2 access token for authorization: firefly_iii_auth
        configuration = firefly_iii_client.Configuration(
            host=os.getenv("FIREFLY_HOST"), access_token=os.getenv("FIREFLY_PAT")
        )

        self.akahu_headers = akahu2firefly.get_akahu_headers()

        self.dbcon = db_manager("idmappings.sqlite3")

        # Load mapping of akahu account ids to firefly account ids from local sqlite mappings db
        self.create_mapping_dicts_from_db()

        with firefly_iii_client.ApiClient(configuration) as self.api_client:
            print("Hydrating accounts")
            # Load accounts from both firefly and akahu
            self.hydrate_firefly_accounts()
            self.hydrate_akahu_accounts()

            print("Creating missing accounts")
            # Create any accounts missing in firefly
            # self.create_missing_accounts_in_firefly()

            # Recreate the mapping dicts with updated data as needed
            self.create_mapping_dicts_from_db()

            # Fetch and load transactions from akahu api into session table
            # TODO use date of last recorded transaction as starting point
            print("Fetching transactions")
            self.hydrate_transactions()
            print("Updating record table")
            # Compare record table to the current session, update & create any rows in record table as needed
            self.compare_session_table_to_record_table()

            # ================================================
            # At this point, we now have an up to date record
            # of bank transactions locally in the sqlite
            # records table and can process based on that
            # ================================================

            # Try to find the oldest starting balance we have in transaction record table
            # for our firefly accounts and update their starting value to that
            print("update firefly account balance")
            self.update_starting_balance_for_firefly_accounts()

            # Look for any transactions not in the firefly mapping table (e.g not yet created)
            # or with a new updated_at time (e.g needs update)
            print("Updating firefly transactions")
            self.compare_record_table_to_firefly_table()

    def update_starting_balance_for_firefly_accounts(self):
        """
        Find the earliest transaction we have in the records store for every firefly account
        And set the opening balance and opening balance dates to the balance that was recorded
        at that transaction time
        """
        for akahu_account_id, firefly_account_id in self.akahu2firefly.items():
            result = self.dbcon.execute(
                """
                SELECT balance, amount, created_at
                  FROM akahu_transaction_record
                  WHERE account = ? 
               ORDER BY created_at ASC
                  LIMIT 1
                """,
                [akahu_account_id],
            ).fetchone()
            if result:
                balance, amount, timestamp = result
                starting_balance = balance + (amount * -1)
                dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                accounts_api_client = accounts_api.AccountsApi(self.api_client)
                account: AccountSingle = accounts_api_client.get_account(
                    firefly_account_id
                )
                attributes = account.data["attributes"]
                update = AccountUpdate(
                    attributes["name"],
                    opening_balance=str(starting_balance),
                    opening_balance_date=dt.date(),
                )
                result: AccountSingle = accounts_api_client.update_account(
                    firefly_account_id, update
                )

    def create_mapping_dicts_from_db(self):
        mappings = self.dbcon.execute(
            "SELECT akahu_account_id, firefly_account_id from akahu2firefly_account"
        ).fetchall()
        for (
            akahu_account_id,
            firefly_account_id,
        ) in mappings:
            self.akahu2firefly[akahu_account_id] = firefly_account_id
            self.firefly2akahu[firefly_account_id] = akahu_account_id

    def hydrate_transactions(self):
        cursor = True
        # Clear the session storage before refreshing it
        self.dbcon.execute("""DELETE FROM akahu_transaction_session""")
        self.dbcon.commit()

        while cursor:
            if cursor:
                # url = "https://api.akahu.io/v1/transactions?start=2022-09-25"
                # TODO make this update automtaically
                url = "https://api.akahu.io/v1/transactions?start=2023-05-01"
            else:
                url = "https://api.akahu.io/v1/transactions?cursor=" + cursor
            response = requests.request("GET", url, headers=self.akahu_headers)

            # Convert json response to dict
            transactions = loads(response.text)

            cursor = transactions["cursor"]["next"]
            for transaction in transactions["items"]:
                self.store_transaction_in_session(transaction)

    def compare_record_table_to_firefly_table(self):
        # Get any new and updated records to create
        add_or_update = self.dbcon.execute(
            """
               SELECT r.body,
                      t.firefly_trans_id
                 FROM akahu_transaction_record r
            LEFT JOIN akahu2firefly_transaction t
                   ON r.transaction_id = t.akahu_trans_id
                WHERE t.akahu_trans_id IS NULL
                   OR t.updated_at != r.updated_at
            """
        )
        for body, firefly_trans_id in add_or_update:
            if firefly_trans_id:
                self.update_firefly_transaction_record(loads(body), firefly_trans_id)
            else:
                self.store_firefly_transaction_record(loads(body))

    def compare_session_table_to_record_table(self):
        # Get any new and updated records
        add_or_update = self.dbcon.execute(
            """
               SELECT s.body,
                 CASE
                      WHEN s.updated_at != r.updated_at
                      THEN 1
                      ELSE 0
                  END as needs_update
                 FROM akahu_transaction_session s
            LEFT JOIN akahu_transaction_record r
                   ON r.transaction_id = s.transaction_id
                WHERE r.transaction_id IS NULL
                   OR r.updated_at != s.updated_at
            """
        )
        for body, needs_update in add_or_update:
            if needs_update == 1:
                self.update_transaction_record(loads(body))
            else:
                self.store_transaction_record(loads(body))

    def update_transaction_record(self, akahu_transaction):
        akahu_transid = akahu_transaction["_id"]
        akahu_account_id = akahu_transaction["_account"]
        akahu_user_id = akahu_transaction["_user"]
        akahu_transaction_created_at = parser.parse(
            akahu_transaction["date"]
        ).timestamp()
        akahu_updated_at = parser.parse(akahu_transaction["updated_at"]).timestamp()
        akahu_amount = float(akahu_transaction["amount"])
        akahu_balance = float(akahu_transaction["balance"])
        akahu_description = self.get_description_string(akahu_transaction)
        akahu_date = akahu_transaction["date"]
        akahu_body = dumps(akahu_transaction)
        akahu_type = akahu_transaction["type"]
        self.dbcon.execute(
            """
                UPDATE akahu_transaction_record
                   SET account = ?,
                       user = ?,
                       date = ?,
                       balance = ?,
                       type = ?,
                       body = ?,
                       amount = ?,
                       created_at = ?,
                       updated_at = ?,
                       description = ?
                 WHERE transaction_id = ?
            """,
            [
                akahu_account_id,
                akahu_user_id,
                akahu_date,
                akahu_balance,
                akahu_type,
                akahu_body,
                akahu_amount,
                akahu_transaction_created_at,
                akahu_updated_at,
                akahu_description,
                akahu_transid,
            ],
        )
        self.dbcon.commit()

    def update_firefly_transaction_record(
        self, akahu_transaction, firefly_transaction_id
    ):
        # TODO
        print(
            f"update firefly transaction {firefly_transaction_id} from akahu_transaction {akahu_transaction['_id']}"
        )

    def store_firefly_transaction_record(self, akahu_transaction):
        if akahu_transaction["type"] == "TRANSFER":
            self.create_kiwibank_transfer(akahu_transaction)
        elif akahu_transaction["amount"] < 0:
            self.create_withdrawal(akahu_transaction)
        elif akahu_transaction["amount"] > 0:
            self.create_deposit(akahu_transaction)
        else:
            print("Uknown transaction type")
            print(akahu_transaction)

    def store_transaction_in_session(self, akahu_transaction):
        akahu_transid = akahu_transaction["_id"]
        akahu_account_id = akahu_transaction["_account"]
        akahu_user_id = akahu_transaction["_user"]
        akahu_transaction_created_at = parser.parse(
            akahu_transaction["date"]
        ).timestamp()
        akahu_updated_at = parser.parse(akahu_transaction["updated_at"]).timestamp()
        akahu_amount = float(akahu_transaction["amount"])
        akahu_balance = float(akahu_transaction["balance"])
        akahu_description = self.get_description_string(akahu_transaction)
        akahu_date = akahu_transaction["date"]
        akahu_body = dumps(akahu_transaction)
        akahu_type = akahu_transaction["type"]
        self.dbcon.execute(
            """INSERT INTO akahu_transaction_session
                    VALUES 
                    (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    )
            """,
            [
                akahu_transid,
                akahu_account_id,
                akahu_user_id,
                akahu_date,
                akahu_balance,
                akahu_type,
                akahu_body,
                akahu_amount,
                akahu_transaction_created_at,
                akahu_updated_at,
                akahu_description,
            ],
        )
        self.dbcon.commit()

    def store_transaction_record(self, akahu_transaction):
        akahu_transid = akahu_transaction["_id"]
        akahu_account_id = akahu_transaction["_account"]
        akahu_user_id = akahu_transaction["_user"]
        akahu_transaction_created_at = parser.parse(
            akahu_transaction["date"]
        ).timestamp()
        akahu_updated_at = parser.parse(akahu_transaction["updated_at"]).timestamp()
        akahu_amount = float(akahu_transaction["amount"])
        akahu_balance = float(akahu_transaction["balance"])
        akahu_description = self.get_description_string(akahu_transaction)
        akahu_date = akahu_transaction["date"]
        akahu_body = dumps(akahu_transaction)
        akahu_type = akahu_transaction["type"]
        self.dbcon.execute(
            """INSERT INTO akahu_transaction_record
                    VALUES 
                    (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    )
            """,
            [
                akahu_transid,
                akahu_account_id,
                akahu_user_id,
                akahu_date,
                akahu_balance,
                akahu_type,
                akahu_body,
                akahu_amount,
                akahu_transaction_created_at,
                akahu_updated_at,
                akahu_description,
            ],
        )
        self.dbcon.commit()

    def create_kiwibank_transfer(self, akahu_transaction):
        # Because akahu transactions on kiwibank do not have a target account, we have to parse the description with regex
        # Im sure this will never go wrong at any point
        description = akahu_transaction["description"]
        matcher = re.compile(
            "(?P<control>TRANSFER FROM|TRANSFER TO).+ - (?P<account>[0-9][0-9])"
        )
        match = matcher.match(description)
        if len(match.groups()) != 2:
            print(
                f"unable to match transfer description as expected {akahu_transaction['id']}"
            )
            return
        direction, target = match.groups()
        if direction == "TRANSFER TO":
            target_firefly_account_id = self.firefly_accounts_by_number[target]
        else:
            return  # we choose one direction to record in firefly
        self.create_transfer(akahu_transaction, target_firefly_account_id)

    def create_transfer(self, akahu_transaction, target_firefly_account_id):
        category, tags = self.get_category_and_tags(akahu_transaction)

        source_firefly_account_id = self.akahu2firefly[akahu_transaction["_account"]]

        akahu_transaction_id = akahu_transaction["_id"]
        akahu_transaction_updated_at = parser.parse(
            akahu_transaction["updated_at"]
        ).timestamp()
        transaction_api_client = transactions_api.TransactionsApi(self.api_client)
        transaction_store = TransactionStore(
            apply_rules=True,
            error_if_duplicate_hash=False,
            fire_webhooks=True,
            group_title=akahu_transaction["description"],
            transactions=[
                TransactionSplitStore(
                    source_id=source_firefly_account_id,
                    type=TransactionTypeProperty("transfer"),
                    destination_id=target_firefly_account_id,
                    amount=str(abs(akahu_transaction["amount"])),
                    category_name=category,
                    date=parser.parse(akahu_transaction["date"]),
                    description=self.get_description_string(akahu_transaction),
                    notes="Created by akahu2firefly",
                    reconciled=True,
                    tags=tags,
                ),
            ],
        )  # TransactionStore | JSON array or key=value pairs with the necessary transaction information. See the model for the exact specifications.
        try:
            # Store a new transaction
            api_response = transaction_api_client.store_transaction(transaction_store)
            data: TransactionRead = api_response.data
            # Store the resulting transaction mapping
            self.dbcon.execute(
                """INSERT OR REPLACE INTO akahu2firefly_transaction VALUES (?, ?, ?)""",
                [akahu_transaction_id, data.id, akahu_transaction_updated_at],
            )
            self.dbcon.commit()
        except firefly_iii_client.ApiException as e:
            print("Exception when calling TransactionsApi->store_transaction: %s\n" % e)

    def get_description_string(self, akahu_transaction):
        merchant = self.get_merchant(akahu_transaction)
        description = akahu_transaction["description"]
        if merchant:
            description += " Merchant:" + merchant
        return description

    def get_merchant(self, akahu_transaction):
        if "merchant" in akahu_transaction:
            return akahu_transaction["merchant"]["name"]
        return ""

    def get_category_and_tags(self, akahu_transaction):
        category = None
        tags = []
        if (
            "category" in akahu_transaction
            and "components" in akahu_transaction["category"]
        ):
            for component in akahu_transaction["category"]["components"]:
                tags.append(component["name"])
                if component["type"] == "nzfcc:pfm":
                    category = component["name"]
        return category, tags

    def create_withdrawal(self, akahu_transaction):
        category, tags = self.get_category_and_tags(akahu_transaction)
        merchant = self.get_merchant(akahu_transaction)

        firefly_account_id = self.akahu2firefly[akahu_transaction["_account"]]
        akahu_transaction_id = akahu_transaction["_id"]
        akahu_transaction_updated_at = parser.parse(
            akahu_transaction["updated_at"]
        ).timestamp()
        transaction_api_client = transactions_api.TransactionsApi(self.api_client)
        transaction_store = TransactionStore(
            apply_rules=True,
            error_if_duplicate_hash=False,
            fire_webhooks=True,
            group_title=akahu_transaction["description"],
            transactions=[
                TransactionSplitStore(
                    amount=str(abs(akahu_transaction["amount"])),
                    category_name=category,
                    date=parser.parse(akahu_transaction["date"]),
                    description=self.get_description_string(akahu_transaction),
                    notes="Created by akahu2firefly",
                    reconciled=True,
                    source_id=firefly_account_id,
                    tags=tags,
                    type=TransactionTypeProperty("withdrawal"),
                    destination_name=merchant,
                ),
            ],
        )  # TransactionStore | JSON array or key=value pairs with the necessary transaction information. See the model for the exact specifications.

        try:
            # Store a new transaction
            api_response = transaction_api_client.store_transaction(transaction_store)
            data: TransactionRead = api_response.data
            # Store the resulting transaction mapping
            self.dbcon.execute(
                """INSERT OR REPLACE INTO akahu2firefly_transaction VALUES (?, ?, ?)""",
                [akahu_transaction_id, data.id, akahu_transaction_updated_at],
            )
            self.dbcon.commit()

        except firefly_iii_client.ApiException as e:
            print("Exception when calling TransactionsApi->store_transaction: %s\n" % e)

    def create_deposit(self, akahu_transaction):
        category, tags = self.get_category_and_tags(akahu_transaction)
        merchant = self.get_merchant(akahu_transaction)

        firefly_account = self.akahu2firefly[akahu_transaction["_account"]]

        akahu_transaction_id = akahu_transaction["_id"]
        akahu_transaction_updated_at = parser.parse(
            akahu_transaction["updated_at"]
        ).timestamp()
        transaction_api_client = transactions_api.TransactionsApi(self.api_client)
        transaction_store = TransactionStore(
            apply_rules=True,
            error_if_duplicate_hash=False,
            fire_webhooks=True,
            group_title=akahu_transaction["description"],
            transactions=[
                TransactionSplitStore(
                    amount=str(abs(akahu_transaction["amount"])),
                    category_name=category,
                    date=parser.parse(akahu_transaction["date"]),
                    description=self.get_description_string(akahu_transaction),
                    notes="Created by akahu2firefly",
                    reconciled=True,
                    destination_id=firefly_account,
                    tags=tags,
                    type=TransactionTypeProperty("deposit"),
                    source_name=merchant,
                ),
            ],
        )  # TransactionStore | JSON array or key=value pairs with the necessary transaction information. See the model for the exact specifications.

        try:
            # Store a new transaction
            api_response = transaction_api_client.store_transaction(transaction_store)
            data: TransactionRead = api_response.data
            # Store the resulting transaction mapping
            self.dbcon.execute(
                """INSERT OR REPLACE INTO akahu2firefly_transaction VALUES (?, ?, ?)""",
                [akahu_transaction_id, data.id, akahu_transaction_updated_at],
            )
            self.dbcon.commit()
        except firefly_iii_client.ApiException as e:
            print("Exception when calling TransactionsApi->store_transaction: %s\n" % e)

    def create_missing_accounts_in_firefly(self):
        for account_id, account in self.akahu_accounts_by_account_id.items():
            if account_id not in self.akahu2firefly:
                self.create_account_in_firefly(account, account_id)

    def create_account_in_firefly(self, account, akahu_account_id):
        accounts_api_client = accounts_api.AccountsApi(self.api_client)
        to_be_created = AccountStore(
            account_number=account["formatted_account"],
            account_role=AccountRoleProperty("savingAsset"),
            currency_code=account["balance"]["currency"],
            include_net_worth=True,
            name=account["name"],
            notes=account["name"],
            type=ShortAccountTypeProperty("asset"),
        )
        result: AccountSingle = accounts_api_client.store_account(to_be_created)
        data: AccountRead = result.data
        # Store the resulting account mapping
        self.dbcon.execute(
            """INSERT OR REPLACE INTO akahu2firefly_account VALUES (?, ?)""",
            [akahu_account_id, data.id],
        )
        self.dbcon.commit()

    def hydrate_firefly_accounts(self):
        # First hydrate the accounts from firefly
        accounts_api_client = accounts_api.AccountsApi(self.api_client)
        firefly_accounts: AccountArray = accounts_api_client.list_account(type="asset")
        for firefly_account in firefly_accounts.data:
            attributes = firefly_account["attributes"]
            self.firefly_accounts_by_account_id[firefly_account.id] = attributes
            if attributes["account_number"]:
                number = re.match(
                    r"\d\d-\d\d\d\d-\d\d\d\d\d\d\d-(\d\d)", attributes["account_number"]
                )
                self.firefly_accounts_by_number[number.groups()[0]] = firefly_account.id

    def hydrate_akahu_accounts(self):
        url = "https://api.akahu.io/v1/accounts"
        response = requests.request("GET", url, headers=self.akahu_headers)
        akahu_accounts = loads(response.text)
        for akahu_account in akahu_accounts["items"]:
            akahu_account_id = akahu_account["_id"]
            self.akahu_accounts_by_account_id[akahu_account_id] = akahu_account


if __name__ == "__main__":
    app = akahu2firefly()
    app.main()
