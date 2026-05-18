def gray_code(n):
    """
    Generates an n-bit Gray code sequence.

    Args:
        n (int): Number of bits.

    Returns:
        list: Gray code sequence.
    """
    res = []
    for i in range(1 << n):
        res.append(i ^ (i >> 1))
    return res


if __name__ == "__main__":
    print(f"2-bit Gray code: {gray_code(2)}")
    print(f"3-bit Gray code: {gray_code(3)}")
