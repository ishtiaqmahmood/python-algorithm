def get_distinct_prime_factors(n):
    factors = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0: temp //= d
        d += 1
    if temp > 1: factors.add(temp)
    return factors


def is_sphenic(n):
    """
    Checks if n is a sphenic number (product of 3 distinct primes).
    """
    factors = get_distinct_prime_factors(n)
    if len(factors) != 3: return False
    prod = 1
    for f in factors: prod *= f
    return prod == n


if __name__ == "__main__":
    for i in [30, 42, 60]:
        print(f"Is {i} sphenic? {is_sphenic(i)}")
