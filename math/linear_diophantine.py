def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def find_any_solution(a, b, c):
    """
    Finds any solution to the linear Diophantine equation ax + by = c.

    Args:
        a (int): Coefficient a.
        b (int): Coefficient b.
        c (int): Constant c.

    Returns:
        tuple: (x, y, g) where ax + by = c, or None if no solution exists.
    """
    g, x0, y0 = extended_gcd(abs(a), abs(b))
    if c % g != 0:
        return None
    x = x0 * (c // g)
    y = y0 * (c // g)
    if a < 0:
        x = -x
    if b < 0:
        y = -y
    return x, y, g


if __name__ == "__main__":
    a, b, c = 10, 6, 14
    sol = find_any_solution(a, b, c)
    if sol:
        x, y, g = sol
        print(f"Solution to {a}x + {b}y = {c} is x={x}, y={y}")
    else:
        print(f"No solution to {a}x + {b}y = {c}")
