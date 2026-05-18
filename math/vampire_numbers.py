def is_vampire(n):
    """
    Checks if n is a vampire number.
    """
    s = str(n)
    if len(s) % 2 != 0: return False

    from itertools import permutations
    digits = list(s)
    for p in permutations(digits):
        f1 = int("".join(p[:len(s)//2]))
        f2 = int("".join(p[len(s)//2:]))
        if f1 * f2 == n:
            if not (str(f1).endswith('0') and str(f2).endswith('0')):
                return True
    return False


if __name__ == "__main__":
    print(f"Is 1260 vampire? {is_vampire(1260)}")
