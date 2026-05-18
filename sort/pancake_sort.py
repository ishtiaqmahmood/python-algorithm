def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1


def pancake_sort(arr):
    """
    Pancake Sort.
    """
    curr_size = len(arr)
    while curr_size > 1:
        mi = arr.index(max(arr[0:curr_size]))
        if mi != curr_size - 1:
            flip(arr, mi)
            flip(arr, curr_size - 1)
        curr_size -= 1
    return arr


if __name__ == "__main__":
    print(f"Pancake Sort: {pancake_sort([23, 10, 20, 11, 12, 6, 7])}")
