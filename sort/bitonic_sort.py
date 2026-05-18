def bitonic_compare(arr, i, j, dire):
    if (dire == 1 and arr[i] > arr[j]) or (dire == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]


def bitonic_merge(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            bitonic_compare(arr, i, i + k, dire)
        bitonic_merge(arr, low, k, dire)
        bitonic_merge(arr, low + k, k, dire)


def bitonic_sort_rec(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort_rec(arr, low, k, 1)
        bitonic_sort_rec(arr, low + k, k, 0)
        bitonic_merge(arr, low, cnt, dire)


def bitonic_sort(arr):
    """
    Bitonic Sort (Works for power-of-2 length).
    """
    bitonic_sort_rec(arr, 0, len(arr), 1)
    return arr


if __name__ == "__main__":
    arr = [3, 7, 4, 8, 6, 2, 1, 5]
    print(f"Bitonic Sort: {bitonic_sort(arr)}")
