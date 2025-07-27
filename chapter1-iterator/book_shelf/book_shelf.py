from dataclasses import dataclass, field
from book import Book
from interface import MyIterable, MyIterator


@dataclass
class BookShelf(MyIterable[Book]):
    _books: list[Book] = field(default_factory=list[Book])
    _last: int = 0

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books.append(book)
        self._last += 1

    def get_length(self) -> int:
        return self._last

    def iterator(self) -> MyIterator[Book]:
        # NOTE: ここでimportしないと循環参照になる。Javaの書き方に寄せているから？
        from book_shelf_iterator import BookShelfIterator
        return BookShelfIterator(self)

