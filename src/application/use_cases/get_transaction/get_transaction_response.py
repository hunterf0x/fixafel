from src.application.application_response import ApplicationResponse


class GetTransactionResponse(ApplicationResponse):
    def __init__(self, trx):
        self.transaction = trx

    def to_json(self) -> dict:
        return {
            "TrxNro": self.transaction.trxNro,
            "PK_Store": self.transaction.pk_store,
            "PK_Terminal": self.transaction.pk_terminal,
            "PK_TransactionNo": self.transaction.pk_transaction_no,
            "body": self.transaction.body,
            "trxRcp": self.transaction.trxRcp,
            "status": self.transaction.status,
            "trxDocType": self.transaction.trxDocType
        }