from typing import override
from banner import Banner
from print import Print


class PrintBannerDeligation(Print):

    def __init__(self, _string: str) -> None:
        self._banner = Banner(_string)

    @override
    def print_weak(self) -> None:
        self._banner.show_with_paren()

    @override
    def print_strong(self) -> None:
        self._banner.show_with_aster()
