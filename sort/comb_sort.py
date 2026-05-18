def comb_sort(arr):
    """
    Comb Sort.
    """
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted_flag = False
    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
    return arr


if __name__ == "__main__":
    print(f"Comb Sort: {comb_sort([8, 4, 1, 56, 3, -44, 23, -6, 28, 0])}")
