from abc import ABC, abstractmethod


class Product(ABC):
    """
    Factory によって生成されるインスタンス
    """
    @abstractmethod
    def use(self) -> None: ...
