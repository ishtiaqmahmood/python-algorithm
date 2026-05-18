def int_to_roman(num):
    """
    Converts an integer to a Roman numeral.

    Args:
        num (int): Input integer.

    Returns:
        str: Roman numeral representation.
    """
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


if __name__ == "__main__":
    for i in [3, 4, 9, 58, 1994]:
        print(f"{i} = {int_to_roman(i)}")
