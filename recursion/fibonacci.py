def fibonacci(n):
    """
    Computes the nth Fibonacci number.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The nth Fibonacci number.
    """
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative or a non-integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    test_n = 10
    print(f"Fibonacci of {test_n} is {fibonacci(test_n)}")
