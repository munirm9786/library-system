import unittest
from book import Book  # Import Book class
from library_system import HashMap  # Import HashMap class
from merge_sort import merge_sort  # Import merge_sort function


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        # Initialize the hash map and add test books
        self.hash_map = HashMap()
        self.books = [
            Book("12345", "A Tale of Two Cities", "Charles Dickens", 1859),
            Book("67890", "1984", "George Orwell", 1949),
            Book("54321", "Brave New World", "Aldous Huxley", 1932),
        ]
        for book in self.books:
            self.hash_map.add_book(book)

    def test_add_book(self):
        # Test adding a new book and checking its existence
        new_book = Book("99999", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        result = self.hash_map.add_book(new_book)
        self.assertEqual(result, "Book added successfully.")
        self.assertEqual(self.hash_map.search("99999").title, "The Great Gatsby")

    def test_search_book(self):
        # Test searching for an existing book by ISBN
        found_book = self.hash_map.search("12345")
        self.assertEqual(found_book.title, "A Tale of Two Cities")

    def test_remove_book(self):
        # Test removing an existing book and verifying removal
        result = self.hash_map.remove_book("12345")
        self.assertEqual(result, "Book removed successfully.")
        self.assertEqual(self.hash_map.search("12345"), "Book not found.")

    def test_merge_sort_by_title(self):
        # Test sorting books by their title
        sorted_books = merge_sort(self.books, "title")
        self.assertEqual([book.title for book in sorted_books], [
            "1984",
            "A Tale of Two Cities",
            "Brave New World"
        ])

    def test_merge_sort_empty_list(self):
        # Test sorting an empty list (edge case)
        self.assertEqual(merge_sort([], "title"), [])


if __name__ == "__main__":
    unittest.main()
