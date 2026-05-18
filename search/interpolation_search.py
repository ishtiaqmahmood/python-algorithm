def interpolation_search(arr, x):
    """
    Interpolation Search.
    """
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x: return low
            return -1

        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

        if arr[pos] == x: return pos
        if arr[pos] < x: low = pos + 1
        else: high = pos - 1
    return -1


if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    print(f"Interpolation Search (x=18): {interpolation_search(arr, 18)}")
