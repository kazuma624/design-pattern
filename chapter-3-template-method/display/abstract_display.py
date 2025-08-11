from abc import ABC, abstractmethod


class AbstractDisplay(ABC):
    @abstractmethod
    def open(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def print(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError

    def display(self) -> None:
        self.open()
        for i in range(5):
            self.print()
        self.close()
