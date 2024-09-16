"""This module defines the ApplicationResponse abstract base class."""

from abc import ABC, abstractmethod


class ApplicationResponse(ABC):
    """Abstract base class for application responses."""
    # pylint: disable=too-few-public-methods
    @abstractmethod
    def to_json(self) -> dict:
        """Converts the response to a JSON-serializable dictionary.

        Returns:
            dict: The JSON-serializable dictionary representing the response.
        """
        raise NotImplementedError
