from abc import abstractmethod
from typing import Optional

from src.domain.transaction import Transaction


class TrxRepository:
    @abstractmethod
    def find_one(self, id: str, attr: str) -> Optional[Transaction]: raise NotImplementedError
