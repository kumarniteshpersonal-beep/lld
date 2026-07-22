class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

# client code
collection = BookCollection()
collection.add_book("book1")
collection.add_book("book2")
books = collection.get_books()

# first book
print(books[0])

# problems:
# 1. tomorrow if I changed the underlying data structure from list to set, then the client code will break because sets do not support indexing.
# 2. Hence iterator pattern make sure that client code does't need to be changed if we change the underlying data structure of the collection.
