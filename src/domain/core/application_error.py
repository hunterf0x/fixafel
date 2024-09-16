"""This module defines the ApplicationError class for handling application errors."""

class ApplicationError(Exception):
    """Base class for application-specific exceptions."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
