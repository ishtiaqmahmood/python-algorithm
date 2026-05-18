from functools import reduce


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("modInverse does not exist")
    return (x % m + m) % m


def chinese_remainder_theorem(n, a):
    """
    Solves a system of linear congruences using the Chinese Remainder Theorem.
    x ≡ a[i] (mod n[i])

    Args:
        n (list): List of moduli.
        a (list): List of remainders.

    Returns:
        int: Solution to the system of congruences.
    """
    total_prod = reduce(lambda x, y: x * y, n)
    result = 0
    for n_i, a_i in zip(n, a):
        p = total_prod // n_i
        result += a_i * mod_inverse(p, n_i) * p
    return result % total_prod


if __name__ == "__main__":
    n = [3, 4, 5]
    a = [2, 3, 1]
    # x ≡ 2 (mod 3)
    # x ≡ 3 (mod 4)
    # x ≡ 1 (mod 5)
    print(f"Result of CRT is {chinese_remainder_theorem(n, a)}")
