import sqlite3
from models import akahu2firefly_transaction

class db_manager:
    def __init__(self, filename) -> None:
        self.dbcon = sqlite3.connect(filename)
        self.setup_tables()

    def setup_tables(self):
        self.dbcon.execute(
            """
            CREATE TABLE IF NOT EXISTS akahu2firefly_account
                (
                    akahu_account_id TEXT UNIQUE NOT NULL, firefly_account_id TEXT NOT NULL
                )
            """
        )
        self.dbcon.execute(
            """
            CREATE TABLE IF NOT EXISTS akahu2firefly_transaction
                (
                    akahu_trans_id TEXT UNIQUE NOT NULL,
                    firefly_trans_id TEXT NOT NULL,
                    updated_at INT
                )
            """
        )
        self.dbcon.execute(
            """
            CREATE TABLE IF NOT EXISTS akahu_transaction_record
                (
                    transaction_id TEXT UNIQUE NOT NULL,
                    account TEXT NOT NULL,
                    user TEXT NOT NULL,
                    date TEXT NOT NULL,
                    balance REAL NOT NULL,
                    type TEXT NOT NULL,
                    body TEXT NOT NULL,
                    amount REAL NOT NULL,
                    created_at INT NOT NULL,
                    updated_at INT NOT NULL,
                    description TEXT NOT NULL
                )
            """
        )
        self.dbcon.execute(
            """
            CREATE TABLE IF NOT EXISTS akahu_transaction_session
                (
                    transaction_id TEXT UNIQUE NOT NULL,
                    account TEXT NOT NULL,
                    user TEXT NOT NULL,
                    date TEXT NOT NULL,
                    balance REAL NOT NULL,
                    type TEXT NOT NULL,
                    body TEXT NOT NULL,
                    amount REAL NOT NULL,
                    created_at INT NOT NULL,
                    updated_at INT NOT NULL,
                    description TEXT NOT NULL
                )
            """
        )
        self.dbcon.commit()

    def execute(self, sql, *args):
        return self.dbcon.execute(sql, *args)

    def commit(self):
        return self.dbcon.commit()

    def get_most_recent_mapping_transaction(self) -> akahu2firefly_transaction:
        cursor = self.dbcon.execute("""SELECT * FROM akahu2firefly_transaction ORDER BY updated_at DESC LIMIT 1""")
        result = cursor.fetchone()
        if result:
            result = akahu2firefly_transaction(*result)
        else:
            result = None
        return result

    def get_firefly_account_for_akahu_account(self, akahu_account_id):
        mapping = self.dbcon.execute(
            """
                SELECT akahu_account_id, firefly_account_id
                  FROM akahu2firefly_account
                 WHERE akahu_account_id = ?
            """,
            [akahu_account_id],
        ).fetchone()
        if mapping:
            return mapping[1]
        else:
            return None
