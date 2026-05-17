def insertion_sort(custom_list):
    """
    Performs insertion sort to sort a list in ascending order.

    Args:
        custom_list (list): The list to be sorted.
    """
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j + 1] = custom_list[j]
            j -= 1
        custom_list[j + 1] = key
    print(custom_list)


if __name__ == "__main__":
    test_list = [4, 9, 5, 1, 7, 3, 8, 2, 6]
    insertion_sort(test_list)
