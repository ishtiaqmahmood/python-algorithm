def legendre_symbol(a, p):
    """
    Returns the Legendre symbol (a/p).
    """
    res = pow(a, (p - 1) // 2, p)
    return -1 if res == p - 1 else res


def shanks_tonelli(n, p):
    """
    Shanks-Tonelli algorithm to solve x^2 ≡ n (mod p).

    Args:
        n (int): Integer.
        p (int): Prime.

    Returns:
        int: One of the square roots, or None.
    """
    if legendre_symbol(n, p) != 1: return None
    if n % p == 0: return 0
    if p == 2: return p
    if p % 4 == 3: return pow(n, (p + 1) // 4, p)

    s, q = 0, p - 1
    while q % 2 == 0:
        s += 1
        q //= 2

    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t % p != 1:
        i, temp_t = 0, t
        while temp_t % p != 1:
            i += 1
            temp_t = pow(temp_t, 2, p)
        b = pow(c, pow(2, m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p
    return r


if __name__ == "__main__":
    print(f"Square root of 5 mod 41: {shanks_tonelli(5, 41)}")
