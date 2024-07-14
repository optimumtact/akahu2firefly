from datetime import datetime


class akahu2firefly_transaction:
    def __init__(self, akahu_trans_id: str, firefly_trans_id: str, updated_at: float) -> None:
        self.akahu_trans_id = akahu_trans_id
        self.firefly_trans_id = firefly_trans_id,
        self.updated_at = datetime.fromtimestamp(updated_at)

    def __str__(self) -> str:
        return f"""{self.akahu_trans_id} -> {self.firefly_trans_id} : {self.updated_at}"""

    def __repr__(self) -> str:
        return f"""{self.akahu_trans_id} -> {self.firefly_trans_id} : {self.updated_at}"""
