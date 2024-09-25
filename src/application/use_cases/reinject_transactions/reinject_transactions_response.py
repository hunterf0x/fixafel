"""This module defines the response for reinjecting transactions."""

from application.application_response import ApplicationResponse

class ReinjectedTransactionsResponse(ApplicationResponse):
    """Response for reinjecting transactions."""

    def __init__(self, transactions):
        """Initializes the response with the given transactions.

        Args:
            transactions (list): The list of transactions.
        """
        self.transactions = transactions

    def to_json(self) -> list[dict]:
        """Converts the transactions to a JSON-serializable format.

        Returns:
            list[dict]: The list of transactions in JSON format.
        """
        print(self.transactions)
        return [
            {
                "TrxNro": trx.trx_nro
            }
            for trx in self.transactions
        ]

    def get_transaction_count(self) -> int: # IA idea
        """Gets the count of transactions.

        Returns:
            int: The number of transactions.
        """
        return len(self.transactions)
