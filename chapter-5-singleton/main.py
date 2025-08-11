from singleton import Singleton


def main():
    print("Start.")
    obj1: Singleton = Singleton()
    obj2: Singleton = Singleton()

    if obj1 is obj2:
        print("obj1とobj2は同じインスタンスです。")
    else:
        print("obj1とobj2は同じインスタンスではありません。")

    print("End.")


if __name__ == "__main__":
    main()
    """
    Start.
    インスタンスを生成しました。
    インスタンスを生成しました。
    obj1とobj2は同じインスタンスです。
    End.
    """

    # Singleton.__new__ をコメントアウトしてから実行するとこうなる
    """
    Start.
    インスタンスを生成しました。
    インスタンスを生成しました。
    obj1とobj2は同じインスタンスではありません。
    End.
    """
