def ternary_search(arr, key):
    """
    Performs iterative ternary search to find the index of a key in a sorted array.

    Args:
        arr (list): A sorted list of elements.
        key: The element to search for.

    Returns:
        int: The index of the key if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2

        if key < arr[mid1]:
            high = mid1 - 1
        elif key > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_key = 5

    result = ternary_search(test_arr, test_key)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element is not found in array")
