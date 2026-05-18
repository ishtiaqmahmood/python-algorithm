def factorial_mod_p(n, p):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % p
    return res


def wilsons_theorem(p):
    """
    Checks if a number is prime using Wilson's Theorem.
    (p-1)! ≡ -1 (mod p) if and only if p is prime.

    Args:
        p (int): Number to check.

    Returns:
        bool: True if prime, False otherwise.
    """
    if p <= 1:
        return False
    if p == 2:
        return True
    return factorial_mod_p(p - 1, p) == (p - 1)


if __name__ == "__main__":
    p = 7
    print(f"Is {p} prime? {wilsons_theorem(p)}")
    p = 10
    print(f"Is {p} prime? {wilsons_theorem(p)}")
