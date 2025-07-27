from book import Book
from book_shelf import BookShelf
from dataclasses import dataclass
from interface import MyIterator
from typing import override


@dataclass
class BookShelfIterator(MyIterator[Book]):
    _book_shelf: BookShelf
    _index: int = 0

    @override
    def has_next(self) -> bool:
        return self._index < self._book_shelf.get_length()

    @override
    def next(self) -> Book:
        if not self.has_next():
            raise IndexError
        book: Book = self._book_shelf.get_book_at(self._index)
        self._index += 1
        return book
