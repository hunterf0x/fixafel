"""This module defines the command for reinjecting transactions."""

from application.application_command import ApplicationCommand

class ReinjectTransactionsCommand(ApplicationCommand):
    """Command for reinjecting transactions."""

    def __init__(self, transactions: list):
        """Initializes the command with the given list of transactions.

        Args:
            transactions (list): The list of transactions to reinject.
        """
        self.__transactions = transactions

    @property
    def transaction_list(self) -> list:
        """Gets the list of transactions.

        Returns:
            list: The list of transactions.
        """
        return self.__transactions

    def add_transaction(self, transaction: dict): # IA idea
        """Adds a transaction to the list.

        Args:
            transaction (dict): The transaction to add.
        """
        self.__transactions.append(transaction)
