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
        """これがテンプレートメソッド
        内部で呼び出しているメソッドは具象クラスで実装しないといけない
        """
        self.open()
        for i in range(5):
            self.print()
        self.close()
