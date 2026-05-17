def factorial(n):
    """
    Computes the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(4))
