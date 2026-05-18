import math


def sieve(limit):
    """
    Standard Sieve of Eratosthenes to find primes up to limit.
    """
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes


def segmented_sieve(l, r):
    """
    Finds all prime numbers in the range [l, r] using the Segmented Sieve.

    Args:
        l (int): Lower bound.
        r (int): Upper bound.

    Returns:
        list: Primes in [l, r]
    """
    limit = int(math.sqrt(r))
    primes = sieve(limit)

    is_prime = [True] * (r - l + 1)
    if l == 1:
        is_prime[0] = False

    for p in primes:
        start = max(p * p, (l + p - 1) // p * p)
        for i in range(start, r + 1, p):
            is_prime[i - l] = False

    result = []
    for i in range(l, r + 1):
        if is_prime[i - l]:
            result.append(i)
    return result


if __name__ == "__main__":
    l, r = 10, 50
    print(f"Primes between {l} and {r}: {segmented_sieve(l, r)}")
