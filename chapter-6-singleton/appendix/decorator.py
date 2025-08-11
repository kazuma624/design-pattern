def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class MyClass:
    def __init__(self):
        print("インスタンスを生成しました。")


if __name__ == "__main__":
    a = MyClass()
    b = MyClass()

    print(a is b)
