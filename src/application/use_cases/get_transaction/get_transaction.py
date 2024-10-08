"""This module contains the GetTransactionUseCase class, which handles the logic for retrieving a transaction."""

from application.application_service import ApplicationService
from application.use_cases.get_transaction.get_transaction_command import GetTransactionCommand
from application.use_cases.get_transaction.get_transaction_response import GetTransactionResponse
from domain.trx_not_found_error import TrxNotFoundError
from domain.trx_repository import TrxRepository
from domain.transaction import Transaction


class GetTransactionUseCase(ApplicationService):
    """Handles the logic for retrieving a transaction."""
    # pylint: disable=too-few-public-methods
    def __init__(self, trx_repository: TrxRepository, logger):
        self.trx_repository = trx_repository
        self.logger = logger

    def execute(self, command: GetTransactionCommand) -> GetTransactionResponse:
        """Executes the use case to retrieve a transaction based on the given command.

        Args:
            command (GetTransactionCommand): The command containing the transaction param and attributes.

        Returns:
            GetTransactionResponse: The response containing the retrieved transaction.

        Raises:
            TrxNotFoundError: If the transaction is not found.
        """
        trx: Transaction = self.trx_repository.find_one(command.param, command.attr)

        if trx is None:
            raise TrxNotFoundError('Trx not found')

        return GetTransactionResponse(trx)
