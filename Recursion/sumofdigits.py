def sum_of_digits(n):
    """
    Computes the sum of digits of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The sum of digits of n.
    """
    assert n >= 0 and int(n) == n, 'The number has to be positive integer only'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n / 10))

if __name__ == "__main__":
    test_n = 123
    print(f"Sum of digits of {test_n} is {sum_of_digits(test_n)}")
