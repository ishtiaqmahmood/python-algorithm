def gray_code(n):
    """
    Generates n-bit Gray code.
    """
    res = []
    for i in range(1 << n):
        res.append(i ^ (i >> 1))
    return res


if __name__ == "__main__":
    print(f"3-bit Gray code: {gray_code(3)}")
