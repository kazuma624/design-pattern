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

    factory.get_owner_by_id(101)
    factory.get_owner_by_id(102)
    factory.get_owner_by_id(103)


if __name__ == "__main__":
    main()
    """
    Hiroshi Yukiのカードを作ります。
    [IDCard:(101) Hiroshi Yuki]を登録しました。
    Tomuraのカードを作ります。
    [IDCard:(102) Tomura]を登録しました。
    Hanako Satoのカードを作ります。
    [IDCard:(103) Hanako Sato]を登録しました。
    [IDCard:(101) Hiroshi Yuki]を使います。
    [IDCard:(102) Tomura]を使います。
    [IDCard:(103) Hanako Sato]を使います。
    ID:103はIDCard:Hiroshi Yukiです。
    ID:103はIDCard:Tomuraです。
    """
