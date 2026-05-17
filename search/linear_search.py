def linear_search(arr, x):
    """
    Performs linear search to find the index of an element in an array.

    Args:
        arr (list): The list of elements.
        x: The element to search for.

    Returns:
        int: The index of the element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    test_arr = [2, 5, 4, 7, 6, 3, 9, 8, 1]
    test_x = 6

    result = linear_search(test_arr, test_x)
    if result == -1:
        print("Element is not present in array")
    else:
        print(f"Element is present at index {result}")
