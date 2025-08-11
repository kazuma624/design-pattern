Pythonで実装する方法をChatGPTに尋ねると4パターン出してくれたので、一応全部メモしておいた。

## 明示的な方法

```python
class Singleton:
    _singleton = None

    def __new__(cls):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
        return cls._singleton

    def __init__(self):
        print("インスタンスを生成しました。")

```

わかりやすさ重視でこれを採用した。

## デコレータを使う方法

```python
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


a = MyClass()
b = MyClass()

print(a is b)  # True
```

## モジュールを使う方法

よく見るやり方

- settings.py

```python
class Settings:
    pass


# ここで生成する
settings = Settings()
```

- main.py

```python
# ここのインポート文を呼び出すと `settings = Settings()` が1回だけ実行される
from settings import settings


settings.foo = 123

from settings import settings as s2

print(s2.foo)  # 123
```


## メタクラスを使う方法

```python

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=SingletonMeta):
    def __init__(self):
        print("インスタンスを生成しました。")


a = MyClass()
b = MyClass()

print(a is b)  # True
```

シングルトンにしたいクラスはメタクラスに `SingletonMeta` を指定するだけで良い。
複数のクラスをシングルトンにしたい場合は便利。

### (補足)メタクラスの話

メタクラスを指定することと、通常のクラス継承の違いは、
**「継承はインスタンスの振る舞いを変える」のに対して、メタクラスは**
**「クラスそのもの（設計図）の振る舞いを変える」** という点にあります。

---

#### 1. ざっくり言うと

| 項目          | 通常の継承                             | メタクラス指定                                                    |
| ----------- | --------------------------------- | ---------------------------------------------------------- |
| 影響する対象      | **インスタンス**の生成や動作                  | **クラスオブジェクト**の生成や動作                                        |
| フックできるタイミング | `__init__` / `__new__`（インスタンス生成時） | `__new__` / `__init__`（**クラス生成時**） + `__call__`（インスタンス生成時） |
| 使いどころ       | インスタンスの機能追加・共通化                   | クラスの定義ルール、インスタンス生成制御、メソッド自動追加など                            |
| 見た目         | `class A(BaseClass): ...`         | `class A(metaclass=MetaClass): ...`                        |

---

#### 2. 通常の継承の流れ

```python
class Base:
    def hello(self):
        print("Hello from Base")

class Sub(Base):
    pass

obj = Sub()   # Sub のインスタンス生成
obj.hello()   # Base の機能を引き継ぐ
```

* 継承では「インスタンスに持たせる機能」を引き継ぎます。
* クラス定義そのものの作り方には影響しません。

---

#### 3. メタクラスの流れ

```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"クラス {name} を作成中...")
        namespace['greet'] = lambda self: print(f"Hello from {name}")
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()  # ここでクラスの設計図にすでに greet が追加されている
obj.greet()      # Hello from MyClass
```

* メタクラスは **クラスが定義された瞬間** に割り込み可能。
* 上記では、`MyClass` を作るときに `greet` メソッドが勝手に追加されています。
* インスタンス生成だけでなく、クラス生成段階の処理も可能です。

---

