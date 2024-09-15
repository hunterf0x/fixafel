from src.application.application_command import ApplicationCommand


class GetListTransactionsCommand(ApplicationCommand):
    def __init__(self, trx_list: list):
        self.__trx_list = trx_list

    @property
    def trx_list(self) -> list:
        return self.__trx_list
