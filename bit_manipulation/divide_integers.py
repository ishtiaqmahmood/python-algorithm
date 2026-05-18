def divide(dividend, divisor):
    """
    Divide Two Integers without using multiplication, division, and mod operator.
    """
    if dividend == -2147483648 and divisor == -1: return 2147483647

    a, b, res = abs(dividend), abs(divisor), 0
    for x in range(31, -1, -1):
        if (a >> x) >= b:
            res += 1 << x
            a -= b << x
    return res if (dividend > 0) == (divisor > 0) else -res


if __name__ == "__main__":
    print(f"10 / 3 = {divide(10, 3)}")
    print(f"7 / -3 = {divide(7, -3)}")
