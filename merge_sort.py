# Merge sort function to sort books by an attribute
def merge_sort(books, key):
    # Base case for recursion
    if len(books) <= 1:
        return books
    mid = len(books) // 2  # Split the list into halves
    left = merge_sort(books[:mid], key)  # Sort left half
    right = merge_sort(books[mid:], key)  # Sort right half
    return merge(left, right, key)  # Merge sorted halves


# Merge two sorted lists
def merge(left, right, key):
    result = []  # List to store merged results
    i = j = 0  # Pointers for left and right lists

    # Compare and merge
    while i < len(left) and j < len(right):
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])  # Add smaller element
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # Add remaining elements from left
    result.extend(right[j:])  # Add remaining elements from right
    return result
