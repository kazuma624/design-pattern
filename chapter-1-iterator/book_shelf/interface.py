from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar("T")


class MyIterator(ABC, Generic[T]):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def next(self) -> T:
        raise NotImplementedError


class MyIterable(ABC, Generic[T]):
    @abstractmethod
    def iterator(self) -> MyIterator[T]:
        raise NotImplementedError
