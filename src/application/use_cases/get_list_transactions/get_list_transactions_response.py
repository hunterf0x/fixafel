from src.application.application_response import ApplicationResponse


class GetListTransactionsResponse(ApplicationResponse):
    def __init__(self, transactions):
        self.transactions = transactions

    def to_json(self) -> list[dict]:
        return [
            {
                "TrxNro": trx.trxNro,
                "PK_Store": trx.pk_store,
                "PK_Terminal": trx.pk_terminal,
                "PK_TransactionNo": trx.pk_transaction_no,
                "body": trx.body,
                "trxRcp": trx.trxRcp,
                "status": trx.status,
                "trxDocType": trx.trxDocType
            }
            for trx in self.transactions
        ]