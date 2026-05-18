def gcd(a, b):
    while b: a, b = b, a % b
    return a


def is_carmichael(n):
    """
    Checks if n is a Carmichael number.
    """
    if n < 2 or is_prime(n): return False
    for a in range(2, n):
        if gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True


if __name__ == "__main__":
    print(f"Is 561 Carmichael? {is_carmichael(561)}")
