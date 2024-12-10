def test_merge_sort():
    books = [
        Book("123", "Python Basics", "John Doe", 2020),
        Book("456", "Data Structures", "Jane Doe", 2019),
    ]
    #
    sorted_books = merge_sort(books, "name")  
    assert sorted_books[0].title == "Data Structures"  
import unittest
from library-system import Book, HashMap, merge_sort  
class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        """Initialize test data before each test."""
        self.hash_map = HashMap()
        self.books = [
            Book("12345", "A Tale of Two Cities", "Charles Dickens", 1859),
            Book("67890", "1984", "George Orwell", 1949),
            Book("54321", "Brave New World", "Aldous Huxley", 1932),
        ]
        for book in self.books:
            self.hash_map.add_book(book)
    def test_add_book(self):
        """Test adding books to the HashMap."""
        new_book = Book("99999", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        result = self.hash_map.add_book(new_book)
        self.assertEqual(result, "Book added successfully.")
        self.assertEqual(self.hash_map.search("99999").title, "The Great Gatsby")
    def test_add_duplicate_book(self):
        """Test adding a book with an existing ISBN."""
        duplicate_book = Book("12345", "Duplicate Book", "Another Author", 2020)
        result = self.hash_map.add_book(duplicate_book)
        self.assertEqual(result, "Book already exists.")
    def test_search_book(self):
        """Test searching for a book by ISBN."""
        found_book = self.hash_map.search("12345")
        self.assertEqual(found_book.title, "A Tale of Two Cities")
    def test_search_nonexistent_book(self):
        """Test searching for a non-existent book."""
        result = self.hash_map.search("00000")
        self.assertEqual(result, "Book not found.")
    def test_remove_book(self):
        """Test removing a book by ISBN."""
        result = self.hash_map.remove_book("12345")
        self.assertEqual(result, "Book removed successfully.")
        self.assertEqual(self.hash_map.search("12345"), "Book not found.")
    def test_remove_nonexistent_book(self):
        """Test removing a book that doesn't exist."""
        result = self.hash_map.remove_book("00000")
        self.assertEqual(result, "Book not found.")
    def test_merge_sort_by_title(self):
        """Test merge_sort function sorting by title."""
        sorted_books = merge_sort(self.books, "title")
        self.assertEqual([book.title for book in sorted_books], [
            "1984",
            "A Tale of Two Cities",
            "Brave New World"
        ])
    def test_merge_sort_by_year(self):
        """Test merge_sort function sorting by year."""
        sorted_books = merge_sort(self.books, "year")
        self.assertEqual([book.year for book in sorted_books], [1859, 1932, 1949])
    def test_merge_sort_invalid_key(self):
        """Test merge_sort function with an invalid key."""
        with self.assertRaises(AttributeError):
            merge_sort(self.books, "invalid_key")
if __name__ == "__main__":
    unittest.main()
