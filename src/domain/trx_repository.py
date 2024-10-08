"""This module defines the TrxRepository class for handling transaction repository operations."""

from abc import abstractmethod
from typing import Optional
from domain.transaction import Transaction

class TrxRepository:
    """Abstract base class for transaction repository operations."""

    @abstractmethod
    def find_one(self, transaction_param: str, attr: str) -> Optional[Transaction]:
        """Finds a single transaction by its ID and attribute.

        Args:
            transaction_param (str): The param of the transaction search.
            attr (str): The attribute to filter the transaction.

        Returns:
            Optional[Transaction]: The found transaction or None if not found.
        """
        raise NotImplementedError

    @abstractmethod
    def get_list(self, trx_list: list) -> list[Transaction] | None:
        """Gets a list of transactions based on the provided list of IDs.

        Args:
            trx_list (list): The list of transaction IDs.

        Returns:
            list[Transaction] | None: The list of found transactions or None if none are found.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, doc_id: str, attributes: dict) -> Transaction:
        """Updates a transaction with the given attributes.

        Args:
            doc_id (str): The document ID of the transaction to update.
            attributes (dict): The attributes to update in the transaction.

        Returns:
            Transaction: The updated transaction.
        """
        raise NotImplementedError
