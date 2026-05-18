def is_quadratic_residue(a, p):
    """
    Checks if a is a quadratic residue modulo p.
    """
    if a % p == 0: return True
    return pow(a, (p - 1) // 2, p) == 1


if __name__ == "__main__":
    p = 7
    for a in range(p):
        print(f"Is {a} quadratic residue mod {p}? {is_quadratic_residue(a, p)}")
