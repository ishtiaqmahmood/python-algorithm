def counting_sort(arr):
    """
    Counting Sort.
    """
    if not arr: return arr
    max_val = max(arr)
    min_val = min(arr)
    count = [0] * (max_val - min_val + 1)
    for x in arr:
        count[x - min_val] += 1

    res = []
    for i, c in enumerate(count):
        res.extend([i + min_val] * c)
    return res


if __name__ == "__main__":
    print(f"Counting Sort: {counting_sort([4, 2, 2, 8, 3, 3, 1])}")
