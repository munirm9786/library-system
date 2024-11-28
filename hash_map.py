class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.year = year  

    def __repr__(self):
        return f"Book(ISBN={self.isbn}, Title={self.isbn}, Year={self.year})"

class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = None

    def _hash(self, key):
        return hash(key) % self.size

    def add_book(self, book):
        index = self._hash(book.isbn)
        for item in self.buckets[index]:
            if item.isbn == book.isbn:  
                return "Book already exists."
        self.buckets[index].append(book)

    def search(self, isbn):
        index = self._hash(isbn)
        for book in self.buckets[index]:
                return book
        return "Book not found."
