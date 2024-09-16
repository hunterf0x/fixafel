from abc import ABC, abstractmethod
from typing import Any

class BaseController(ABC):
    """Base controller."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def register_routes(self) -> None:
        """Register routes."""
        pass

    @abstractmethod
    def routes(self) -> Any:
        """Get routes."""
        pass
