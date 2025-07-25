from book_shelf import BookShelf
from book import Book
from interface import MyIterable, MyIterator

class Main:
    @staticmethod
    def main():
        book_shelf = BookShelf(4)
        book_shelf.append_book(Book("Around the World in 80 Days"))
        book_shelf.append_book(Book("Bible"))
        book_shelf.append_book(Book("Cinderella"))
        book_shelf.append_book(Book("Daddy-Long-Legs"))

        # 明示的にIteratorを使う方法
        it = book_shelf.iterator()
        while it.has_next():
            book = it.next()
            print(book.get_name())

        print("-" * 32)




if __name__ == "__main__":
    Main.main()
