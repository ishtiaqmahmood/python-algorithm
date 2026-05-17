def binary_search(arr, key):
    """
    Performs iterative binary search to find the index of a key in a sorted array.

    Args:
        arr (list): A sorted list of elements.
        key: The element to search for.

    Returns:
        int: The index of the key if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid

    return -1


def recursive_binary_search(arr, low, high, key):
    """
    Performs recursive binary search to find the index of a key in a sorted array.

    Args:
        arr (list): A sorted list of elements.
        low (int): The starting index of the search range.
        high (int): The ending index of the search range.
        key: The element to search for.

    Returns:
        int: The index of the key if found, otherwise -1.
    """
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return recursive_binary_search(arr, low, mid - 1, key)
        else:
            return recursive_binary_search(arr, mid + 1, high, key)
    else:
        return -1


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_key = 6

    result = binary_search(test_list, test_key)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")
