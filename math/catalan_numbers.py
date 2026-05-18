def catalan_number(n):
    """
    Computes the nth Catalan number.
    C_n = (1 / (n + 1)) * (2n choose n)

    Args:
        n (int): Index.

    Returns:
        int: nth Catalan number.
    """
    if n <= 1:
        return 1

    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            res[i] += res[j] * res[i - j - 1]
    return res[n]


if __name__ == "__main__":
    for i in range(10):
        print(f"C_{i} = {catalan_number(i)}")
