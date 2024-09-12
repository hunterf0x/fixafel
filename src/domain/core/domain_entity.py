from abc import ABC, abstractmethod


class DomainEntity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def to_object(self) -> dict:
        return self.__dict__