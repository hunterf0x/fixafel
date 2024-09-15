from src.application.appliaction_service import ApplicationService
from src.application.use_cases.get_list_transactions.get_list_transactions_command import GetListTransactionsCommand
from src.application.use_cases.get_list_transactions.get_list_transactions_response import GetListTransactionsResponse
from src.domain.trx_not_found_error import TrxNotFoundError
from src.domain.trx_repository import TrxRepository
from src.domain.transaction import Transaction


class GetListTransactionsUseCase(ApplicationService):
    def __init__(self, trx_repository: TrxRepository):
        self.trx_repository = trx_repository

    def execute(self, command: GetListTransactionsCommand) -> GetListTransactionsResponse:
        transactions: list[Transaction] = self.trx_repository.get_list(command.trx_list)
        print(f"TrxUseCases.execute: {transactions}")
        #print(command.attr)


        if transactions is None:
            raise TrxNotFoundError('Trx not found')

        return GetListTransactionsResponse(transactions)