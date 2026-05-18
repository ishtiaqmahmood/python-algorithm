def legendre(a, p):
    """
    Returns Legendre symbol (a/p).
    """
    if a % p == 0: return 0
    res = pow(a, (p - 1) // 2, p)
    return 1 if res == 1 else -1


if __name__ == "__main__":
    print(f"Legendre symbol (5, 7): {legendre(5, 7)}")
