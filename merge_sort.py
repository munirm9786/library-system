def merge_sort(books, key):
    """Performs merge sort on a list of books based on a specified key."""
    if len(books) <= 1:
        return books
    mid = len(books) // 2
        return books  # a list with one or no element is already sortedd
    mid = len(books) // 2  # find the middle index to divide the list
    left = merge_sort(books[:mid], key)
    right = merge_sort(books[mid:], key)
    #merge the sorted halved
    return merge(left, right, key)


@@ -20,7 +21,7 @@ def merge(left, right, key):
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements
    #   Add any remaining elements from the left list if there is any
    result.extend(left[i:])
    result.extend(right[j:])
    result.extend(right[j:])  # Add any remaining elements from the right list if there is any
    return result
