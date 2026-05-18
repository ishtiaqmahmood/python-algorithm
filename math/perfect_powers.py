import math


def is_perfect_power(n):
    """
    Checks if n is a perfect power (n = m^k for k > 1).
    """
    if n < 1: return False
    if n == 1: return True
    for k in range(2, int(math.log2(n)) + 1):
        m = round(n**(1/k))
        if m**k == n: return True
    return False


if __name__ == "__main__":
    for i in [4, 8, 9, 10]:
        print(f"Is {i} perfect power? {is_perfect_power(i)}")
