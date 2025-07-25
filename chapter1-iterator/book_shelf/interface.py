from abc import ABC, abstractmethod
from typing import TypeVar


T = TypeVar("T")

class MyIterator:
    @abstractmethod
    def has_next() -> bool:
        raise NotImplementedError

    @abstractmethod
    def next() -> T:
        raise NotImplementedError


class MyIterable:
    @abstractmethod
    def iterator() -> T:
        raise NotImplementedError
