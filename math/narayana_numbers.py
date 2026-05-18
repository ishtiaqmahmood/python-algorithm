def nCr(n, r):
    if r < 0 or r > n: return 0
    if r == 0 or r == n: return 1
    if r > n // 2: r = n - r
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res


def narayana_number(n, k):
    """
    Narayana number N(n, k) = (1/n) * C(n, k) * C(n, k-1).
    """
    return (nCr(n, k) * nCr(n, k - 1)) // n


if __name__ == "__main__":
    print(f"N(3, 2) = {narayana_number(3, 2)}")
