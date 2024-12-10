def merge_sort(books, key):
    # Perform merge sort on a list of books by a specified key
    if len(books) <= 1:
        return books
    mid = len(books) // 2  # Split the list into two halves
    left = merge_sort(books[:mid], key)  # Sort the left half
    right = merge_sort(books[mid:], key)  # Sort the right half
    return merge(left, right, key)  # Merge the sorted halves


def merge(left, right, key):
    # Merge two sorted lists based on the specified key
    result = []
    i = j = 0  # Initialize pointers for left and right lists

    while i < len(left) and j < len(right):
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])  # Add smaller element from left
            i += 1
        else:
            result.append(right[j])  # Add smaller element from right
            j += 1

    result.extend(left[i:])  # Add remaining elements from left
    result.extend(right[j:])  # Add remaining elements from right
    return result
