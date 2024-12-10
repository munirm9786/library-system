# Book class to store book details
class Book:
    def __init__(self, isbn, title, author, year):
        # Initialize book attributes
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        # String representation of the book
        return f"Book(ISBN={self.isbn}, Title={self.title}, Author={self.author}, Year={self.year})"


# HashMap class to store and manage books
class HashMap:
    def __init__(self, size=100):
        # Initialize hash map with buckets
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Calculate bucket index
        return hash(key) % self.size

    def add_book(self, book):
        # Add a book to the hash map
        index = self._hash(book.isbn)
        for item in self.buckets[index]:
            if item.isbn == book.isbn:  # Check for duplicate ISBN
                return "Book already exists."
        self.buckets[index].append(book)
        return "Book added successfully."

    def search(self, isbn):
        # Search for a book by ISBN
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.isbn == isbn:
                return book
        return "Book not found."

    def remove_book(self, isbn):
        # Remove a book by ISBN
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.isbn == isbn:
                self.buckets[index].remove(book)
                return "Book removed successfully."
        return "Book not found."
