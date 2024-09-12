from src.domain.core.application_error import ApplicationError


class TrxNotFoundError(ApplicationError):
    def __init__(self, message):
        super().__init__(message)