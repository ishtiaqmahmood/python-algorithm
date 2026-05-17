def count_set_bits(n):
    """
    Counts the number of set bits (1s) in an integer (Hamming Weight).

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
    num = 11 # 1011 in binary
    print(f"Set bits in {num}: {count_set_bits(num)}")
