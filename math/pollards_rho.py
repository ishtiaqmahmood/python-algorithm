import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res


def pollards_rho(n):
    """
    Pollard's rho algorithm for integer factorization.
    Finds a non-trivial factor of n.

    Args:
        n (int): Number to factorize.

    Returns:
        int: A factor of n.
    """
    if n % 2 == 0:
        return 2
    if n == 1:
        return 1

    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1

    while g == 1:
        x = (power(x, 2, n) + c) % n
        y = (power(y, 2, n) + c) % n
        y = (power(y, 2, n) + c) % n
        g = gcd(abs(x - y), n)
        if g == n:
            return pollards_rho(n)
    return g


if __name__ == "__main__":
    n = 8051  # 83 * 97
    print(f"A factor of {n} is {pollards_rho(n)}")
