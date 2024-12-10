def merge_sort(books, key):
    """Performs merge sort on a list of books based on a specified key."""
    if len(books) <= 1:
        return books
    mid = len(books) // 2
    left = merge_sort(books[:mid], key)
    right = merge_sort(books[mid:], key)
    return merge(left, right, key)


def merge(left, right, key):
    """Merges two sorted lists into one based on a specified key."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Compare based on the key attribute
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
