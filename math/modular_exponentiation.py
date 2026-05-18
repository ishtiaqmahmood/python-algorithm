def power(a, b, m):
    """
    Computes (a^b) % m efficiently using binary exponentiation.

    Args:
        a (int): Base.
        b (int): Exponent.
        m (int): Modulus.

    Returns:
        int: (a^b) % m
    """
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res


if __name__ == "__main__":
    a, b, m = 2, 10, 1000
    print(f"({a}^{b}) % {m} = {power(a, b, m)}")
