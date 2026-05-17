def sieve_of_eratosthenes(n):
    """
    Finds all prime numbers up to n.

    Args:
        n (int): Upper bound.

    Returns:
        list: List of prime numbers.
    """
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]


if __name__ == "__main__":
    num = 30
    print(f"Primes up to {num}: {sieve_of_eratosthenes(num)}")
