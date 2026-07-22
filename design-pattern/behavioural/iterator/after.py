class BookCollection: # iterable
    def __init__(self):
        self.books = set()

    def add_book(self, book):
        self.books.add(book)

    def get_books(self):
        return self.books
    
    def __iter__(self):
        return BookIterator(self)

class BookIterator: # iterator
    def __init__(self, collection: BookCollection):
        self.collection = collection
        self.iterator = iter(self.collection.get_books()) # set built in iterator

    def __iter__(self): # due this function python will treat this class as an iterable and hence we can use for loop on this class
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            raise StopIteration

# client code
collection = BookCollection()
collection.add_book("book1")
collection.add_book("book2")

book_iterator = iter(BookIterator(collection))
print(next(book_iterator)) # first book

# print all remainging books
for book in book_iterator:
    print(book)