"""This module contains the GetListTransactionsResponse class,
 which encapsulates the response for a list of transactions."""

from application.application_response import ApplicationResponse


class GetListTransactionsResponse(ApplicationResponse):
    """Encapsulates the response for a list of transactions."""
    # pylint: disable=too-few-public-methods
    def __init__(self, transactions):
        """Initializes the GetListTransactionsResponse with the given list of transactions.

        Args:
            transactions: The list of transaction objects.
        """
        self.transactions = transactions

    def to_json(self) -> list[dict]:
        """Converts the list of transactions to a JSON-serializable list of dictionaries.

        Returns:
            list[dict]: The JSON-serializable list representing the transactions.
        """
        return [
            {
                "_id": trx.doc_id,
                "id": trx.transaction_id,
                "TrxNro": trx.trx_nro,
                "PK_Store": trx.pk_store,
                "PK_Terminal": trx.pk_terminal,
                "PK_TransactionNo": trx.pk_transaction_no,
                "body": trx.body,
                "trxRcp": trx.trx_rcp,
                "status": trx.status,
                "trxDocType": trx.trx_doc_type,
                "note": trx.note
            }
            for trx in self.transactions
        ]
