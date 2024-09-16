"""This module defines the BaseController class for handling HTTP routes."""

from abc import ABC, abstractmethod
from typing import Any

class BaseController(ABC):
    """Abstract base class for HTTP controllers."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def register_routes(self) -> None:
        """Register the routes for the controller."""
        pass

    @abstractmethod
    def routes(self) -> Any:
        """Return the routes for the controller."""
        pass
