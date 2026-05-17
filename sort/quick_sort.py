def partition(custom_list, low, high):
    """
    Helper function for quick sort to partition the list.

    Args:
        custom_list (list): The list to be partitioned.
        low (int): The starting index.
        high (int): The ending index.

    Returns:
        int: The index of the pivot element.
    """
    i = low - 1
    pivot = custom_list[high]
    for j in range(low, high):
        if custom_list[j] <= pivot:
            i += 1
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    custom_list[i + 1], custom_list[high] = custom_list[high], custom_list[i + 1]
    return i + 1


def quick_sort(custom_list, low, high):
    """
    Performs quick sort on a list.

    Args:
        custom_list (list): The list to be sorted.
        low (int): Starting index.
        high (int): Ending index.
    """
    if low < high:
        pi = partition(custom_list, low, high)
        quick_sort(custom_list, low, pi - 1)
        quick_sort(custom_list, pi + 1, high)


if __name__ == "__main__":
    test_list = [3, 5, 8, 1, 2, 9, 4, 7, 6]
    quick_sort(test_list, 0, len(test_list) - 1)
    print(test_list)
