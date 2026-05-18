def extended_gcd(a, b):
    """
    Computes the greatest common divisor of a and b, and the coefficients
    x and y such that ax + by = gcd(a, b).

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        tuple: (gcd, x, y)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


if __name__ == "__main__":
    a, b = 35, 15
    g, x, y = extended_gcd(a, b)
    print(f"gcd({a}, {b}) = {g}, x = {x}, y = {y}")
    print(f"{a}*({x}) + {b}*({y}) = {a*x + b*y}")
