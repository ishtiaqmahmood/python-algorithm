def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): Input number.

    Returns:
        bool: True if prime, False otherwise.
    """
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


if __name__ == "__main__":
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 15 prime? {is_prime(15)}")
