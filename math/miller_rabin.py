import random


def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res


def miller_rabin(n, k=5):
    """
    Probabilistic primality test. Returns True if n is probably prime,
    False if n is composite.

    Args:
        n (int): Number to test.
        k (int): Number of iterations.

    Returns:
        bool: Primality result.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    num = 10**9 + 7
    print(f"Is {num} prime? {miller_rabin(num)}")
    num = 10**9 + 9
    print(f"Is {num} prime? {miller_rabin(num)}")
