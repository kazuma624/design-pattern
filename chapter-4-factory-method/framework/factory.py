from abc import ABC, abstractmethod
from framework.product import Product


class Factory(ABC):
    """
    Productクラスのインスタンスを生成することだけを知ってる

    「実際のインスタンス生成を、インスタンス生成のためのメソッド呼び出しに代えることで、
    具体的なクラス名による束縛からスーパークラスを解放している」
    """
    def create(self, owner: str) -> Product:
        p: Product = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner: str) -> Product: ...

    @abstractmethod
    def register_product(self, product: Product) -> None: ...


