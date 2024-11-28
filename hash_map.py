class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add_book(self, book):
        index = self._hash(book.isbn)
        for item in self.buckets[index]:
            if item.isbn = book.isbn:
                return "Book already exists."
        self.buckets[index].append(book)

    def search(self, isbn):
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.title == isbn:
                return book
        return "Book not found."
