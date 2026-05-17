def prime_factorization(n):
    """
    Finds the prime factors of an integer.

    Args:
        n (int): Input integer.

    Returns:
        list: List of prime factors.
    """
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors


if __name__ == "__main__":
    num = 315
    print(f"Prime factors of {num}: {prime_factorization(num)}")
