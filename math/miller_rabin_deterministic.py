def miller_rabin_deterministic(n):
    """
    Deterministic Miller-Rabin test for n < 3,317,044,064,679,887,361.
    """
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Bases for deterministic test
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n == a: return True
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True


if __name__ == "__main__":
    print(f"Is 1000000007 prime? {miller_rabin_deterministic(1000000007)}")
