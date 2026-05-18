def sum_proper_divisors(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0: s += i
    return s


def are_friendly(a, b):
    """
    Checks if two numbers are friendly (same abundancy index).
    """
    from math import gcd
    def abundancy(n):
        s = sum_proper_divisors(n) + n
        g = gcd(s, n)
        return (s // g, n // g)

    return abundancy(a) == abundancy(b)


if __name__ == "__main__":
    print(f"Are 6 and 28 friendly? {are_friendly(6, 28)}")
