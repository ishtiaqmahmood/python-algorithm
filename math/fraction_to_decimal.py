def fraction_to_decimal(numerator, denominator):
    """
    Converts a fraction to its decimal representation as a string.

    Args:
        numerator (int): Numerator.
        denominator (int): Denominator.

    Returns:
        str: Decimal string.
    """
    if numerator == 0:
        return "0"
    res = []
    if (numerator < 0) ^ (denominator < 0):
        res.append("-")

    numerator, denominator = abs(numerator), abs(denominator)
    res.append(str(numerator // denominator))
    remainder = numerator % denominator
    if remainder == 0:
        return "".join(res)

    res.append(".")
    seen = {}
    while remainder != 0:
        if remainder in seen:
            res.insert(seen[remainder], "(")
            res.append(")")
            break
        seen[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator
    return "".join(res)


if __name__ == "__main__":
    print(f"1/2 = {fraction_to_decimal(1, 2)}")
    print(f"2/3 = {fraction_to_decimal(2, 3)}")
    print(f"4/333 = {fraction_to_decimal(4, 333)}")
