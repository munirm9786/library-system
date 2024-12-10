class Book:
    def __init__(self, isbn, title, author, year):
        """Initialize a Book object."""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        """String representation of a Book."""
        return f"Book(ISBN={self.isbn}, Title={self.title}, Author={self.author}, Year={self.year})"

