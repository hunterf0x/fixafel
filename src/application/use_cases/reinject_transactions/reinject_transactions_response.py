
from application.application_response import ApplicationResponse


class ReinjectedTransactionsResponse(ApplicationResponse):
    def __init__(self, transactions):
        self.transactions = transactions

    def to_json(self) -> list[dict]:
        return [
            {
                "TrxNro": trx.trxNro
            }
            for trx in self.transactions
        ]