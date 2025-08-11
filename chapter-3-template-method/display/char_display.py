from abstract_display import AbstractDisplay
from typing import override


class CharDisplay(AbstractDisplay):
    def __init__(self, ch: str) -> None:
        # Python は char と string を区別しないので、あくまで書籍の流れを再現
        self.ch = ch

    @override
    def open(self) -> None:
        print("<<", end="")

    @override
    def print(self) -> None:
        print(self.ch, end="")

    @override
    def close(self) -> None:
        print(">>")
