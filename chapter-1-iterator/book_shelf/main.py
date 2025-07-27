from book_shelf import BookShelf
from book import Book


def main() -> None:
    book_shelf = BookShelf()
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))

    # 明示的にIteratorを使う方法
    it = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(book.get_name())


if __name__ == "__main__":
    main()
