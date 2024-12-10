from library_system import Book

class Book:
    def __init__(self, isbn, title, author, year):
        #book attributes
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):   #string represntation of a book
        return f"Book(ISBN={self.isbn}, Title={self.title}, Year={self.year})"


class HashMap:
    def __init__(self, size=100):
        self.size = size
        # hashmap size and buckets
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
       #calcuulates the bucket index
        return hash(key) % self.size

    def add_book(self, book):
        #Adds a book to the hash map
        index = self._hash(book.isbn)
        for item in self.buckets[index]:
            if item.isbn == book.isbn:  # Check for duplicate ISBN
                return "Book already exists."
        self.buckets[index].append(book)
        return "Book added successfully."

    def search(self, isbn):  #search for book by isbn
        """Searches for a book by ISBN."""
        index = self._hash(isbn)
        for book in self.buckets[index]:
            if book.isbn == isbn:
                return book
        return "Book not found."

   def remove_book(self, isbn):
    """Removes a book by ISBN."""
    index = self._hash(isbn)
    for book in self.buckets[index]:
        if book.isbn == isbn:
            self.buckets[index].remove(book)
            return "Book removed successfully."
    return "Book not found."



    def __repr__(self):  # string representation of hash map
        return f"HashMap({self.buckets})"


# Example usage
hash_map = HashMap()
book1 = Book("12345", "Book One", "Author A", 2020)
book2 = Book("67890", "Book Two", "Author B", 2019)

print(hash_map.add_book(book1))  # add book1
print(hash_map.add_book(book2))  # add book2
print(hash_map.search("12345"))  # search for book1
print(hash_map.remove_book("12345"))  #remove book1
print(hash_map.search("12345"))  # search for removed book

