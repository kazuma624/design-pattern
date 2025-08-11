from abstract_display import AbstractDisplay
from char_display import CharDisplay
from string_display import StringDisplay


def main():
    # スーパークラス型の変数に、サブクラスのインスタンスのどれを代入しても正しく動作するようにする
    # (LSP: The Liskov Substitution Principle)
    d1: AbstractDisplay = CharDisplay("H")

    d2: AbstractDisplay = StringDisplay("Hello, world.")

    d1.display()
    """
    <<HHHHH>>
    """

    d2.display()
    """
    +-------------+
    |Hello, world.|
    |Hello, world.|
    |Hello, world.|
    |Hello, world.|
    |Hello, world.|
    +-------------+
    """


if __name__ == "__main__":
    main()
