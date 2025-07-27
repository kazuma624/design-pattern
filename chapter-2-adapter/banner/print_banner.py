from dataclasses import dataclass
from typing import override
from banner import Banner
from print import Print


@dataclass
class PrintBanner(Banner, Print):
    @override
    def print_weak(self) -> None:
        super().show_with_paren()

    @override
    def print_strong(self) -> None:
        super().show_with_aster()
