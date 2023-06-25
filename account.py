import logging
import json
import requests
import sys
from dotenv import load_dotenv
from db_manager import db_manager
from akahu2firefly import akahu2firefly


class Account:
    def __init__(self, akahu_account_id: str, dbcon: db_manager) -> None:
        self.log = logging.getLogger("akahu2firefly.accounts")
        self.log.debug(f"Creating account manager for {akahu_account_id}")
        self.akahu_account_id = akahu_account_id
        self.akahu_headers = akahu2firefly.get_akahu_headers()
        self.dbcon = dbcon

        self.firefly_account_id = self.dbcon.get_firefly_account_for_akahu_account(
            self.akahu_account_id
        )
        self.log.debug(f"Matched to firefly account {self.firefly_account_id}")

        # this fills out a lot of data on the class, name, balance, type etc
        self.get_akahu_account()

        if not self.firefly_account_id:
            self.create_firefly_account()

    def __str__(self) -> str:
        return f"""{self.name} - {self.type} : {self.balance}, {self.status}"""

    def __repr__(self) -> str:
        return f"""name:{self.name}, akahu_account_id : {self.akahu_account_id}, firefly_account_id : {self.firefly_account_id}, balance : {self.balance}, type : {self.type}"""

    def create_firefly_account(self):
        self.log.debug("Creating firefly account")
        pass

    def get_akahu_account(self):
        self.log.debug("Refreshing account data from akahu api")
        url = f"https://api.akahu.io/v1/accounts/{self.akahu_account_id}"
        response = requests.request("GET", url, headers=self.akahu_headers)
        akahu_account = json.loads(response.text)
        self.log.debug(akahu_account)
        self.akahu_account_data = akahu_account["item"]
        self.name = self.akahu_account_data["name"]
        self.status = self.akahu_account_data["status"]
        self.type = self.akahu_account_data["type"]
        self.balance = self.akahu_account_data["balance"]["current"]

    @staticmethod
    def get_all_akahu_account_ids():
        akahu_headers = akahu2firefly.get_akahu_headers()
        url = "https://api.akahu.io/v1/accounts"
        response = requests.request("GET", url, headers=akahu_headers)
        akahu_accounts = json.loads(response.text)
        account_ids = []
        for akahu_account in akahu_accounts["items"]:
            account_ids.append(akahu_account["_id"])
        return account_ids


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(
        level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)]
    )
    ids = Account.get_all_akahu_account_ids()
    dbcon = db_manager("idmappings.sqlite3")
    accounts = []
    for id in ids:
        print(Account(id, dbcon))
