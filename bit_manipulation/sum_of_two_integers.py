def get_sum(a, b):
    """
    Calculates the sum of two integers without using + or - operators.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: Sum of a and b.
    """
    mask = 0xFFFFFFFF
    while b & mask:
        carry = (a & b) << 1
        a ^= b
        b = carry
    return a & mask if b > 0 else a


if __name__ == "__main__":
    print(f"Sum of 1 and 2: {get_sum(1, 2)}")
