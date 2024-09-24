"""This module contains the GetListTransactionsUseCase class,
which handles the logic for retrieving a list of transactions."""

from application.application_service import ApplicationService
from application.use_cases.get_list_transactions.get_list_transactions_command import GetListTransactionsCommand
from application.use_cases.get_list_transactions.get_list_transactions_response import GetListTransactionsResponse
from domain.trx_not_found_error import TrxNotFoundError
from domain.trx_repository import TrxRepository
from domain.transaction import Transaction


class GetListTransactionsUseCase(ApplicationService):
    """Handles the logic for retrieving a list of transactions."""
    # pylint: disable=too-few-public-methods
    def __init__(self, trx_repository: TrxRepository, logger):
        """Initializes the GetListTransactionsUseCase with the given transaction repository.

        Args:
            trx_repository (TrxRepository): The repository to retrieve transactions from.
        """
        self.trx_repository = trx_repository
        self.logger = logger

    def execute(self, command: GetListTransactionsCommand) -> GetListTransactionsResponse:
        """Executes the use case to retrieve a list of transactions based on the given command.

        Args:
            command (GetListTransactionsCommand): The command containing the list of transaction IDs.

        Returns:
            GetListTransactionsResponse: The response containing the list of retrieved transactions.

        Raises:
            TrxNotFoundError: If no transactions are found.
        """
        transactions: list[Transaction] = self.trx_repository.get_list(command.trx_list)
        print(f"TrxUseCases.execute: {transactions}")

        if transactions is None:
            raise TrxNotFoundError('Trx not found')

        return GetListTransactionsResponse(transactions)
