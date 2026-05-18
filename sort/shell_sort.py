def shell_sort(arr):
    """
    Shell Sort.
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


if __name__ == "__main__":
    print(f"Shell Sort: {shell_sort([12, 34, 54, 2, 3])}")
