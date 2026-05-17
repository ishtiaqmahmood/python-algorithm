def decimal_to_binary(n):
    """
    Converts a decimal integer to its binary representation as an integer of 0s and 1s.

    Args:
        n (int): The decimal integer to convert.

    Returns:
        int: The binary representation.
    """
    assert int(n) == n, 'The parameter must be an integer'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n / 2))

if __name__ == "__main__":
    test_n = 345
    print(f"Decimal {test_n} in binary is {decimal_to_binary(test_n)}")
