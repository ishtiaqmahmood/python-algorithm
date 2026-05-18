import math


def jump_search(arr, x):
    """
    Jump Search.
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n: return -1

    while arr[prev] < x:
        prev += 1
        if prev == min(step, n): return -1

    if arr[prev] == x: return prev
    return -1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    print(f"Jump Search (x=55): {jump_search(arr, 55)}")
