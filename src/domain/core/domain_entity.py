"""This module defines the DomainEntity class for handling domain entities."""

from abc import ABC, abstractmethod

class DomainEntity(ABC):
    """Abstract base class for domain entities."""
    # pylint: disable=too-few-public-methods
    @abstractmethod
    def __init__(self):
        pass

    def to_object(self) -> dict:
        """Converts the domain entity to a dictionary.

        Returns:
            dict: The dictionary representation of the domain entity.
        """
        return self.__dict__
