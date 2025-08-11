from framework.product import Product
from typing import override


class IDCard(Product):
    def __init__(self, owner: str, id: int) -> None:
        print(f"{owner}のカードを作ります。")
        self.owner = owner
        self.id = id

    @override
    def use(self) -> None:
        print(f"{self}を使います。")

    def __str__(self) -> str:
        return f"[IDCard:({self.id}) {self.owner}]"

    def get_owner(self) -> str:
        return self.owner

    def get_id(self) -> int:
        return self.id
