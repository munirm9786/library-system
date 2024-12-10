def merge_sort(books, key):
    """Performs merge sort on a list of books based on a specified key."""
    if len(books) <= 1:
        return books  # a list with one or no element is already sortedd
    mid = len(books) // 2  # find the middle index to divide the list
    left = merge_sort(books[:mid], key)
    right = merge_sort(books[mid:], key)
    #merge the sorted halved
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
    #   Add any remaining elements from the left list if there is any
    result.extend(left[i:])
    result.extend(right[j:])  # Add any remaining elements from the right list if there is any
    return result
