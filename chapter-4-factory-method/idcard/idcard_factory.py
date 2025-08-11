from framework.product import Product
from framework.factory import Factory
from idcard.idcard import IDCard
from typing import override


class IDCardFactory(Factory):

    def __init__(self):
        self.id = 100
        # 解答を見ると演習問題の対応表はこういうイメージではなかったが、
        # 問われている機能は満たしているのでまぁよし
        self._table: dict[int, str] = dict()

    @override
    def create_product(self, owner: str) -> Product:
        self.id += 1
        self._table[self.id] = owner
        return IDCard(owner, self.id)

    @override
    def register_product(self, product: Product) -> None:
        print(f"{product}を登録しました。")

    def get_owner_by_id(self, id: int):
        print(f"ID:{self.id}はIDCard:{self._table[id]}です。")
