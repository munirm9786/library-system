class Book:
    def __init__(self, isbn, title, author, year):
        # Initialize book attributes
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        # Create a string representation for the book
        return f"Book(ISBN={self.isbn}, Title={self.title}, Author={self.author}, Year={self.year})"
