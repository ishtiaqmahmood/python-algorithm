import math


def insertion_sort(custom_list):
    """
    Performs insertion sort to sort a list in ascending order.

    Args:
        custom_list (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j + 1] = custom_list[j]
            j -= 1
        custom_list[j + 1] = key
    return custom_list


def bucket_sort(custom_list):
    """
    Performs bucket sort to sort a list in ascending order.

    Args:
        custom_list (list): The list to be sorted.
    """
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []

    for i in range(number_of_buckets):
        arr.append([])
    for j in custom_list:
        index_b = math.ceil(j * number_of_buckets / max_value)
        arr[index_b - 1].append(j)
    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            custom_list[k] = arr[i][j]
            k += 1
    print(custom_list)


if __name__ == "__main__":
    test_list = [2, 9, 6, 3, 1, 4, 7, 5, 8]
    bucket_sort(test_list)
