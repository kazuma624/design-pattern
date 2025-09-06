

class Triple:
    _instances: dict[str, "Triple"] = dict()
    _max_instances: int = 3

    def __new__(cls, name: str):
        if name in cls._instances:
            return cls._instances[name]
        if len(cls._instances) >= cls._max_instances:
            raise RuntimeError("インスタンスは最大3つまでです")

        _instance = super().__new__(cls)
        cls._instances[name] = _instance
        return _instance

    def __init__(self, name: str) -> None:
        if not hasattr(self, "name"):
            self.name = name
            print("インスタンスを生成しました。")

    @classmethod
    def get_instance(cls, name: str) -> "Triple":
        return cls(name)

    def __str__(self) -> str:
        return self.name

if __name__ == "__main__":
    a1 = Triple.get_instance("ALPHA")
    b1 = Triple.get_instance("BETA")
    c1 = Triple.get_instance("GAMMA")
    a2 = Triple.get_instance("ALPHA")
    b2 = Triple.get_instance("BETA")
    c2 = Triple.get_instance("GAMMA")
    if a1 == a2:
        print("a1 = a2", str(a1))
    else:
        print("a1 != a2")

    if b1 == b2:
        print("b1 = b2", str(b1))
    else:
        print("b1 != b2")

    if c1 == c2:
        print("c1 = c2", str(c1))
    else:
        print("c1 != c2")

    d = Triple.get_instance("DELTA")
