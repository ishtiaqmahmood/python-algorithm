def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def goldbach_conjecture(n):
    """
    Finds two prime numbers that sum up to an even integer n (n > 2).
    According to Goldbach's conjecture, every even integer greater than 2
    is the sum of two primes.

    Args:
        n (int): Even integer.

    Returns:
        tuple: Two primes (p1, p2) such that p1 + p2 = n, or None.
    """
    if n <= 2 or n % 2 != 0:
        return None

    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return i, n - i
    return None


if __name__ == "__main__":
    n = 28
    res = goldbach_conjecture(n)
    if res:
        print(f"{n} = {res[0]} + {res[1]}")
