from src.application.application_command import ApplicationCommand


class GetTransactionCommand(ApplicationCommand):
    def __init__(self, id: str, attribute: str):
        self.__id = id
        self.__attribute = attribute

    @property
    def id(self) -> str:
        return self.__id

    @property
    def attr(self) -> str:
        return self.__attribute