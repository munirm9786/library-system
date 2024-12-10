def merge_sort(books, key):
    #Perform merge sort on a list of books based on a key
    if len(books) <= 1:
        return books  
    mid = len(books) // 2
    left = merge_sort(books[:mid], key)  # Sort the left half
    right = merge_sort(books[mid:], key)  # Sort the right half
    return merge(left, right, key)


def merge(left, right, key):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if getattr(left[i], key) <= getattr(right[j], key):  # Compare by attribute
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Add remaining elements from left
    result.extend(right[j:])  # Add remaining elements from right
    return result
