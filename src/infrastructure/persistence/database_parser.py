"""This module defines the DatabaseParser abstract base class for parsing database objects."""

from abc import ABC, abstractmethod
from domain.core.domain_entity import DomainEntity

class DatabaseParser(ABC):
    """Abstract base class for database parsers."""

    @abstractmethod
    def to_database_object(self, domain: DomainEntity) -> dict:
        """Convert a domain entity to a database object.

        Args:
            domain (DomainEntity): The domain entity to convert.

        Returns:
            dict: The database object representation of the domain entity.
        """
        raise NotImplementedError

    @abstractmethod
    def to_domain_object(self, database_object: dict) -> DomainEntity:
        """Convert a database object to a domain entity.

        Args:
            database_object (dict): The database object to convert.

        Returns:
            DomainEntity: The domain entity representation of the database object.
        """
        raise NotImplementedError
