"""This module contains the GetTransactionResponse class, which encapsulates the response for a transaction."""

from application.application_response import ApplicationResponse


class GetTransactionResponse(ApplicationResponse):
    """Encapsulates the response for a transaction."""
    # pylint: disable=too-few-public-methods
    def __init__(self, trx):
        """Initializes the GetTransactionResponse with the given transaction.

        Args:
            trx: The transaction object.
        """
        self.transaction = trx

    def to_json(self) -> dict:
        """Converts the transaction to a JSON-serializable dictionary.

        Returns:
            dict: The JSON-serializable dictionary representing the transaction.
        """
        return {
            "doc_id": self.transaction.doc_id,
            "id": self.transaction.id,
            "TrxNro": self.transaction.trxNro,
            "PK_Store": self.transaction.pk_store,
            "PK_Terminal": self.transaction.pk_terminal,
            "PK_TransactionNo": self.transaction.pk_transaction_no,
            "body": self.transaction.body,
            "trxRcp": self.transaction.trxRcp,
            "status": self.transaction.status,
            "trxDocType": self.transaction.trxDocType,
            "note": self.transaction.note
        }
