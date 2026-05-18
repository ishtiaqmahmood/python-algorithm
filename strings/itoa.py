def my_itoa(n):
    """
    Converts an integer to a string.

    Args:
        n (int): Input integer.

    Returns:
        str: String representation.
    """
    if n == 0:
        return "0"

    negative = False
    if n < 0:
        negative = True
        n = -n

    res = []
    while n:
        res.append(chr(ord('0') + (n % 10)))
        n //= 10

    if negative:
        res.append('-')

    return "".join(reversed(res))


if __name__ == "__main__":
    for i in [123, -456, 0]:
        print(f"itoa({i}) = '{my_itoa(i)}'")
