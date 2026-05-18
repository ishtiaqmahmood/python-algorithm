def hamming_weight(n):
    """
    Calculates the number of '1' bits in an unsigned integer (also known as Hamming weight).

    Args:
        n (int): Input integer.

    Returns:
        int: Number of set bits.
    """
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count


if __name__ == "__main__":
    n = 11  # 1011 in binary
    print(f"Hamming weight of {n}: {hamming_weight(n)}")
