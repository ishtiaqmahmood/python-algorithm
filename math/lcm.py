def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Calculates the Least Common Multiple of two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: LCM of a and b.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    print(f"LCM of 15 and 20: {lcm(15, 20)}")
