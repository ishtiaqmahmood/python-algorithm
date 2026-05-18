def get_prime_factors(n):
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


def find_primitive_root(p):
    """
    Finds the smallest primitive root modulo p.
    """
    if p == 2: return 1
    phi = p - 1
    factors = get_prime_factors(phi)

    for res in range(2, p):
        ok = True
        for f in factors:
            if pow(res, phi // f, p) == 1:
                ok = False
                break
        if ok: return res
    return None


if __name__ == "__main__":
    print(f"Primitive root of 7: {find_primitive_root(7)}")
    print(f"Primitive root of 11: {find_primitive_root(11)}")
