class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=SingletonMeta):
    def __init__(self):
        print("インスタンスを生成しました。")


if __name__ == "__main__":
    a = MyClass()
    b = MyClass()

    print(a is b)
