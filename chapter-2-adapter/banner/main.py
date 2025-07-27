from print import Print
from print_banner import PrintBanner


def main() -> None:
    p: Print = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == "__main__":
    main()
