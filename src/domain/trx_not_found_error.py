"""This module defines the TrxNotFoundError class for handling transaction not found errors."""

from domain.core.application_error import ApplicationError

class TrxNotFoundError(ApplicationError):
    """Exception raised when a transaction is not found."""
    # pylint: disable=too-few-public-methods
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
