import unittest
from library_system import Book, HashMap
from merge_sort import merge_sort


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap()
        self.books = [
            Book("12345", "A Tale of Two Cities", "Charles Dickens", 1859),
            Book("67890", "1984", "George Orwell", 1949),
            Book("54321", "Brave New World", "Aldous Huxley", 1932),
        ]
        for book in self.books:
            self.hash_map.add_book(book)

    def test_add_book(self):
        # Test adding books
        new_book = Book("99999", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        result = self.hash_map.add_book(new_book)
        self.assertEqual(result, "Book added successfully.")
        self.assertEqual(self.hash_map.search("99999").title, "The Great Gatsby")

    def test_add_duplicate_book(self):
        # Test adding duplicate books
        duplicate_book = Book("12345", "Duplicate Book", "Another Author", 2020)
        result = self.hash_map.add_book(duplicate_book)
        self.assertEqual(result, "Book already exists.")

    def test_search_book(self):
        # Test searching for a book
        found_book = self.hash_map.search("12345")
        self.assertEqual(found_book.title, "A Tale of Two Cities")

    def test_search_nonexistent_book(self):
        # Test searching for a non-existent book
        result = self.hash_map.search("00000")
        self.assertEqual(result, "Book not found.")

    def test_remove_book(self):
        # Test removing a book
        result = self.hash_map.remove_book("12345")
        self.assertEqual(result, "Book removed successfully.")
        self.assertEqual(self.hash_map.search("12345"), "Book not found.")

    def test_merge_sort_by_title(self):
        # Test merge sort by title
        sorted_books = merge_sort(self.books, "title")
        self.assertEqual([book.title for book in sorted_books], [
            "1984",
            "A Tale of Two Cities",
            "Brave New World"
        ])

    def test_merge_sort_empty_list(self):
        # Test merge sort with an empty list
        self.assertEqual(merge_sort([], "title"), [])

    def test_merge_sort_single_element(self):
        # Test merge sort with a single book
        single_book = [Book("99999", "Single Book", "Author X", 2000)]
        self.assertEqual(merge_sort(single_book, "title"), single_book)


if __name__ == "__main__":
    unittest.main()
