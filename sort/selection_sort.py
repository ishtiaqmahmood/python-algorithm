def selection_sort(custom_list):
    """
    Performs selection sort to sort a list in ascending order.

    Args:
        custom_list (list): The list to be sorted.
    """
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i + 1, len(custom_list)):
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)


if __name__ == "__main__":
    test_list = [2, 6, 9, 3, 1, 5, 8, 7, 4]
    selection_sort(test_list)
