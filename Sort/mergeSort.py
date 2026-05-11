def merge(custom_list, l, m, r):
    """
    Merges two subarrays of custom_list.
    First subarray is custom_list[l..m]
    Second subarray is custom_list[m+1..r]

    Args:
        custom_list (list): The list containing subarrays.
        l (int): Left index.
        m (int): Middle index.
        r (int): Right index.
    """
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = custom_list[l + i]

    for j in range(0, n2):
        R[j] = custom_list[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            custom_list[k] = L[i]
            i += 1
        else:
            custom_list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        custom_list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        custom_list[k] = R[j]
        j += 1
        k += 1


def merge_sort(custom_list, l, r):
    """
    Performs merge sort on a list.

    Args:
        custom_list (list): The list to be sorted.
        l (int): Left index.
        r (int): Right index.

    Returns:
        list: The sorted list.
    """
    if l < r:
        m = (l + (r - 1)) // 2
        merge_sort(custom_list, l, m)
        merge_sort(custom_list, m + 1, r)
        merge(custom_list, l, m, r)
    return custom_list


if __name__ == "__main__":
    test_list = [4, 9, 2, 7, 5, 1, 6, 3, 8]
    print(merge_sort(test_list, 0, len(test_list) - 1))
