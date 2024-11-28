def test_merge_sort():
    books = [
        Book("123", "Python Basics", "John Doe", 2020),
        Book("456", "Data Structures", "Jane Doe", 2019),
    ]
    #
    sorted_books = merge_sort(books, "name")  
    assert sorted_books[0].title == "Data Structures"  
