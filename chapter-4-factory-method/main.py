from framework.product import Product
from framework.factory import Factory
from idcard.idcard_factory import IDCardFactory


def main():
    factory: Factory = IDCardFactory()
    card1: Product = factory.create("Hiroshi Yuki")
    card2: Product = factory.create("Tomura")
    card3: Product = factory.create("Hanako Sato")
    card1.use()
    card2.use()
    card3.use()


if __name__ == "__main__":
    main()
    """
    Hiroshi Yukiのカードを作ります。
    [IDCard:Hiroshi Yuki]を登録しました。
    Tomuraのカードを作ります。
    [IDCard:Tomura]を登録しました。
    Hanako Satoのカードを作ります。
    [IDCard:Hanako Sato]を登録しました。
    [IDCard:Hiroshi Yuki]を使います。
    [IDCard:Tomura]を使います。
    [IDCard:Hanako Sato]を使います。
    """
