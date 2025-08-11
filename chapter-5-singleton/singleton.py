class Singleton:
    _singleton = None

    def __new__(cls):
        """
        __new__ はインスタンス生成時、最初に呼ばれる特殊メソッド。
        __init__ はインスタンス生成後に呼び出されるため、シングルトンの管理に使うことはできない
        """
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
        return cls._singleton

    def __init__(self):
        print("インスタンスを生成しました。")
