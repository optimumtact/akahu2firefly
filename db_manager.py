

import sqlite3


class db_manager():
    
    def __init__(self, filename) -> None:
        self.dbcon = sqlite3.connect(filename)
        self.setup_tables()

    def setup_tables(self):
        self.dbcon.execute(
            '''
            CREATE TABLE IF NOT EXISTS akahu2firefly_account
                (
                    akahu_account_id TEXT UNIQUE NOT NULL, firefly_account_id TEXT NOT NULL
                )
            '''
        )
        self.dbcon.execute(
            '''
            CREATE TABLE IF NOT EXISTS akahu2firefly_transaction 
                (
                    akahu_trans_id TEXT UNIQUE NOT NULL,
                    firefly_trans_id TEXT NOT NULL,
                    updated_at INT
                )
            '''
        )
        self.dbcon.execute(
            '''
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
            '''
        )
        self.dbcon.execute(
            '''
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
            '''
        )
        self.dbcon.commit()

    def execute(self, sql, *args):
        return self.dbcon.execute(sql, *args)

    def commit(self):
        return self.dbcon.commit()