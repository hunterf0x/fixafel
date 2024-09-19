"""This module contains the GetTransactionCommand class, which encapsulates the command to get a transaction."""

from application.application_command import ApplicationCommand


class GetTransactionCommand(ApplicationCommand):
    """Encapsulates the command to get a transaction."""
    def __init__(self, transaction_id: str, attribute: str):
        """Initializes the GetTransactionCommand with the given transaction ID and attribute.

        Args:
            transaction_id (str): The ID of the transaction.
            attribute (str): The attribute of the transaction.
        """
        self.__transaction_id = transaction_id
        self.__attribute = attribute

    @property
    def id(self) -> str:
        """Gets the transaction ID.

        Returns:
            str: The transaction ID.
        """
        return self.__transaction_id

    @property
    def attr(self) -> str:
        """Gets the transaction attribute.

        Returns:
            str: The transaction attribute.
        """
        return self.__attribute
