from __future__ import annotations
from dataclasses import dataclass
# from book_shelf import BookShelf
from book import Book
from interface import MyIterator


@dataclass
class BookShelfIterator(MyIterator):
    _book_shelf: "BookShelf"
    _index: int = 0

    def has_next(self) -> bool:
        return self._index < self._book_shelf.get_length()

    def next(self) -> Book:
        if not self.has_next():
            raise IndexError
        book: Book = self._book_shelf.get_book_at(self._index)
        self._index += 1
        return book
