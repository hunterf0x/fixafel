"""This module contains the GetTransactionCommand class, which encapsulates the command to get a transaction."""

from application.application_command import ApplicationCommand


class GetTransactionCommand(ApplicationCommand):
    """Encapsulates the command to get a transaction."""
    def __init__(self, transaction_find: str, attribute: str):
        """Initializes the GetTransactionCommand with the given transaction ID and attribute.

        Args:
            transaction_find (str): The ID of the transaction.
            attribute (str): The attribute of the transaction.
        """
        self.__transaction_find = transaction_find
        self.__attribute = attribute

    @property
    def param(self) -> str:
        """Gets the transaction ID.

        Returns:
            str: The transaction ID.
        """
        return self.__transaction_find

    @property
    def attr(self) -> str:
        """Gets the transaction attribute.

        Returns:
            str: The transaction attribute.
        """
        return self.__attribute
