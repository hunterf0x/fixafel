from application.application_command import ApplicationCommand


class ReinjectTransactionsCommand(ApplicationCommand):
    def __init__(self, transactions: list):
        self.__transactions = transactions

    @property
    def transaction_list(self) -> list:
        return self.__transactions