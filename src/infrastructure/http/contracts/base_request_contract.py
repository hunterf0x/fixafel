"""Module for defining the base request contract."""

from typing import Protocol

class BaseRequestContract(Protocol):
    """Base request contract defining the structure for request contracts."""

    @staticmethod
    def contract() -> dict:
        """Return the JSON schema for the request contract.

        Returns:
            dict: The JSON schema for the request contract.
        """
        pass
