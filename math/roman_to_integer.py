def roman_to_int(s):
    """
    Converts a Roman numeral to an integer.

    Args:
        s (str): Roman numeral.

    Returns:
        int: Integer representation.
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res


if __name__ == "__main__":
    for s in ["III", "IV", "IX", "LVIII", "MCMXCIV"]:
        print(f"{s} = {roman_to_int(s)}")
