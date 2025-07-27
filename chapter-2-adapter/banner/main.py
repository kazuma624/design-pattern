from print import Print
from print_banner import PrintBanner
from print_banner_deligation import PrintBannerDeligation


def main() -> None:
    p: Print = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


def main2() -> None:
    pd: PrintBannerDeligation = PrintBannerDeligation("hello")
    pd.print_weak()
    pd.print_strong()


if __name__ == "__main__":
    main()
    main2()
