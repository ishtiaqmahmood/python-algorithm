def radix_sort(arr):
    """
    Radix Sort (LSD).
    """
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in arr:
            buckets[(x // exp) % 10].append(x)
        arr = [x for b in buckets for x in b]
        exp *= 10
    return arr


if __name__ == "__main__":
    print(f"Radix Sort: {radix_sort([170, 45, 75, 90, 802, 24, 2, 66])}")
