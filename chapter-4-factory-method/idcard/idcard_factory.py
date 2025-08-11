from framework.product import Product
from framework.factory import Factory
from idcard.idcard import IDCard
from typing import override


class IDCardFactory(Factory):
    @override
    def create_product(self, owner: str) -> Product:
        return IDCard(owner)

    @override
    def register_product(self, product: Product) -> None:
        print(f"{product}を登録しました。")
