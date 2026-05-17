def fast_pow(base, exp):
    """
    Calculates (base^exp) efficiently using binary exponentiation.

    Args:
        base (int/float): Base.
        exp (int): Exponent.

    Returns:
        int/float: Result.
    """
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res *= base
        base *= base
        exp //= 2
    return res


if __name__ == "__main__":
    print(f"2^10 = {fast_pow(2, 10)}")
