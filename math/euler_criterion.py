def euler_criterion(a, p):
    """
    Euler's Criterion to check if 'a' is a quadratic residue modulo 'p'.
    """
    if a % p == 0: return 0
    res = pow(a, (p - 1) // 2, p)
    if res == 1: return 1
    return -1


if __name__ == "__main__":
    print(f"Euler criterion (2, 7): {euler_criterion(2, 7)}")
    print(f"Euler criterion (3, 7): {euler_criterion(3, 7)}")
