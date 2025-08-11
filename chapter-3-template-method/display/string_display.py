from abstract_display import AbstractDisplay
from typing import override


class StringDisplay(AbstractDisplay):

    def __init__(self, string: str) -> None:
        self.string = string
        self.width = len(string)

    @override
    def open(self) -> None:
        self._print_line()

    @override
    def print(self) -> None:
        print("|" + self.string + "|")

    @override
    def close(self) -> None:
        self._print_line()

    def _print_line(self) -> None:
        print("+", end="")
        for i in range(self.width):
            print("-", end="")

        print("+")
