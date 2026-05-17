def reverse_bits(n):
    """
    Reverses the bits of a 32-bit unsigned integer.

    Args:
        n (int): Input integer.

    Returns:
        int: Integer with reversed bits.
    """
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


if __name__ == "__main__":
    num = 43261596
    print(f"Reverse bits of {num}: {reverse_bits(num)}")
