from book import Book  # Import Book class

class HashMap:
    def __init__(self, size=100):
        # Initialize the hash map with a fixed size and empty buckets
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Generate a hash index for a given key
        return hash(key) % self.size

    def add_book(self, book):
        # Add a book to the hash map if it's not already present
        index = self._hash(book.isbn)
        for item in self.buckets[index]:
            if item.isbn == book.isbn:  # Check for duplicate ISBNs
                return "Book already exists."
        self.buckets[index].append(book)
        return "Book added successfully."

    def search(self, isbn):
        # Search for a book by its ISBN in the hash map
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.isbn == isbn:
                return book
        return "Book not found."

    def remove_book(self, isbn):
        # Remove a book by its ISBN if it exists in the hash map
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.isbn == isbn:
                self.buckets[index].remove(book)
                return "Book removed successfully."
        return "Book not found."
