from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print_weak(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def print_strong(self) -> None:
        raise NotImplementedError
