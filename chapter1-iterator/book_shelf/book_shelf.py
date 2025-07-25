from dataclasses import dataclass, field
from book import Book
from book_shelf_iterator import BookShelfIterator
from interface import MyIterable


@dataclass
class BookShelf(MyIterable):
    """無理やりJavaの書き方に寄せる"""
    capacity: int

    def __post_init__(self):
        self._books = [None for _ in range(self.capacity)]
        self._last = 0

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books[self._last] = book
        self._last += 1

    def get_length(self) -> int:
        return self._last

    def iterator(self):
        return BookShelfIterator(self)
