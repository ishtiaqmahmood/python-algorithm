def count_bits(n):
    """
    Returns an array of the number of 1s in the binary representation of each number from 0 to n.

    Args:
        n (int): Upper bound.

    Returns:
        list: List of set bit counts.
    """
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res


if __name__ == "__main__":
    print(f"Bit counts for numbers 0 to 5: {count_bits(5)}")
