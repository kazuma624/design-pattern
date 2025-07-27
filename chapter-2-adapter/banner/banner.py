from dataclasses import dataclass


@dataclass
class Banner:
    _string: str

    def show_with_paren(self) -> None:
        print("(" + self._string + ")")

    def show_with_aster(self) -> None:
        print("*" + self._string + "*")
