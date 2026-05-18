import math


def gcd(a, b):
    while b: a, b = b, a % b
    return a


def pollards_p_minus_1(n, b=100):
    """
    Pollard's p-1 algorithm for integer factorization.
    """
    a = 2
    for i in range(2, b + 1):
        a = pow(a, i, n)
    d = gcd(a - 1, n)
    if 1 < d < n: return d
    return None


if __name__ == "__main__":
    n = 1403 # 23 * 61
    print(f"Factor of {n}: {pollards_p_minus_1(n)}")
