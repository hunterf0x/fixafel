from src.application.appliaction_service import ApplicationService
from src.application.use_cases.get_transaction.get_transaction_command import GetTransactionCommand
from src.application.use_cases.get_transaction.get_transaction_response import GetTransactionResponse
from src.domain.trx_not_found_error import TrxNotFoundError
from src.domain.trx_repository import TrxRepository
from src.domain.transaction import Transaction


class GetTransactionUseCase(ApplicationService):
    def __init__(self, trx_repository: TrxRepository):
        self.trx_repository = trx_repository

    def execute(self, command: GetTransactionCommand) -> GetTransactionResponse:
        trx: Transaction = self.trx_repository.find_one(command.id, command.attr)
        print(f"TrxUseCases.execute: {trx}")
        #print(command.attr)


        if trx is None:
            raise TrxNotFoundError('Trx not found')

        return GetTransactionResponse(trx)