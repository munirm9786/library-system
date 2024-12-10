class HashMap:
    def __init__(self, size=100):
        """Initialize the HashMap with a specific size."""
        self.size = size
        self.buckets = [[] for _ in range(self.size)]  # List of buckets

    def _hash(self, key):
        """Compute hash index for a key."""
        return hash(key) % self.size

    def add_book(self, book):
        """Add a book to the hash map."""
        index = self._hash(book.isbn)
        for item in self.buckets[index]:
            if item.isbn == book.isbn:
                return "Book already exists."
        self.buckets[index].append(book)
        return "Book added successfully."

    def search(self, isbn):
        """Search for a book by ISBN."""
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.isbn == isbn:
                return book
        return "Book not found."

    def remove_book(self, isbn):
        """Remove a book by ISBN."""
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.isbn == isbn:
                self.buckets[index].remove(book)
                return "Book removed successfully."
        return "Book not found."
