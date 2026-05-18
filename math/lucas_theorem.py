def nCr_mod_p(n, r, p):
    """
    Calculates nCr % p using dynamic programming.
    """
    if r == 0:
        return 1
    C = [0] * (r + 1)
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            C[j] = (C[j] + C[j - 1]) % p
    return C[r]


def lucas_theorem(n, r, p):
    """
    Computes (nCr) % p using Lucas Theorem for large n and r and small prime p.

    Args:
        n (int): Total elements.
        r (int): Elements to choose.
        p (int): Modulo (must be prime).

    Returns:
        int: (nCr) % p
    """
    if r == 0:
        return 1
    return (lucas_theorem(n // p, r // p, p) * nCr_mod_p(n % p, r % p, p)) % p


if __name__ == "__main__":
    n, r, p = 1000, 300, 13
    print(f"({n}C{r}) % {p} = {lucas_theorem(n, r, p)}")
