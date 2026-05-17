def bubble_sort(custom_list):
    """
    Performs bubble sort to sort a list in ascending order.

    Args:
        custom_list (list): The list to be sorted.
    """
    n = len(custom_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if custom_list[j] > custom_list[j + 1]:
                custom_list[j], custom_list[j + 1] = custom_list[j + 1], custom_list[j]
    print(custom_list)


if __name__ == "__main__":
    test_list = [2, 6, 8, 3, 1, 5, 9, 7]
    bubble_sort(test_list)
