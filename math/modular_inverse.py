def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    """
    Computes the modular multiplicative inverse of a modulo m.
    The inverse exists if and only if a and m are coprime (gcd(a, m) = 1).

    Args:
        a (int): Number.
        m (int): Modulus.

    Returns:
        int: Modular inverse of a modulo m.
    Raises:
        ValueError: If the modular inverse does not exist.
    """
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for {a} mod {m}")
    return (x % m + m) % m


if __name__ == "__main__":
    a, m = 3, 11
    try:
        print(f"Modular inverse of {a} mod {m} is {mod_inverse(a, m)}")
    except ValueError as e:
        print(e)
