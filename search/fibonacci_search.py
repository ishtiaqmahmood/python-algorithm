def fibonacci_search(arr, x):
    """
    Fibonacci Search.
    """
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fibM = fib2 + fib1
    while fibM < n:
        fib2 = fib1
        fib1 = fibM
        fibM = fib2 + fib1

    offset = -1
    while fibM > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < x:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif arr[i] > x:
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return i
    if fib1 and arr[offset + 1] == x: return offset + 1
    return -1


if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    print(f"Fibonacci Search (x=85): {fibonacci_search(arr, 85)}")
