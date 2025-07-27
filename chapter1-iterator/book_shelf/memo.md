## 要点

ループにおいては、iterator のメソッド（`has_next`, `next`）のみが使われている。

```python
it = book_shelf.iterator()
while it.has_next():
    book = it.next()
    print(book.get_name())
```

ループの仕組みを iterator メソッドに全部押し込んでいる。


## 練習問題

Python だと最初から達成されているのでパス。
