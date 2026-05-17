def range_bitwise_and(m, n):
    """
    Returns the bitwise AND of all numbers in range [m, n].

    Args:
        m (int): Start.
        n (int): End.

    Returns:
        int: Result of bitwise AND.
    """
    shift = 0
    while m < n:
        m >>= 1
        n >>= 1
        shift += 1
    return m << shift


if __name__ == "__main__":
    print(f"Bitwise AND of range [5, 7]: {range_bitwise_and(5, 7)}")
