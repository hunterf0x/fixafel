"""This module contains the GetListTransactionsCommand class,
which encapsulates the command to get a list of transactions."""

from src.application.application_command import ApplicationCommand


class GetListTransactionsCommand(ApplicationCommand):
    """Encapsulates the command to get a list of transactions."""
    # pylint: disable=too-few-public-methods
    def __init__(self, trx_list: list):
        """Initializes the GetListTransactionsCommand with the given list of transaction IDs.

        Args:
            trx_list (list): The list of transaction IDs.
        """
        self.__trx_list = trx_list

    @property
    def trx_list(self) -> list:
        """Gets the list of transaction IDs.

        Returns:
            list: The list of transaction IDs.
        """
        return self.__trx_list
