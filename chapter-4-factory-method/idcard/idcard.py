from framework.product import Product
from typing import override


class IDCard(Product):
    def __init__(self, owner: str) -> None:
        print(f"{owner}のカードを作ります。")
        self.owner = owner

    @override
    def use(self) -> None:
        print(f"{self}を使います。")

    def __str__(self) -> str:
        return f"[IDCard:{self.owner}]"

    def get_owner(self) -> str:
        return self.owner
