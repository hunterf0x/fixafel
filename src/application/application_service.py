"""This module defines the ApplicationService abstract base class."""

from abc import ABC, abstractmethod
from application.application_command import ApplicationCommand
from application.application_response import ApplicationResponse


class ApplicationService(ABC):
    """Abstract base class for application services."""
    # pylint: disable=too-few-public-methods
    @abstractmethod
    def execute(self, command: ApplicationCommand) -> ApplicationResponse | None:
        """Executes the given command and returns a response.

        Args:
            command (ApplicationCommand): The command to execute.

        Returns:
            ApplicationResponse | None: The response from executing the command, or None if not applicable.
        """
        raise NotImplementedError
