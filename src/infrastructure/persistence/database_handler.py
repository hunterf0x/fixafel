"""This module defines the DatabaseHandler abstract base class for handling database operations."""

from abc import ABC, abstractmethod
from typing import Any

class DatabaseHandler(ABC):
    """Abstract base class for database handlers."""
    # pylint: disable=too-few-public-methods

    @abstractmethod
    def get_database(self) -> Any:
        """Retrieve the database instance.

        Returns:
            Any: The database instance.
        """
        raise NotImplementedError
