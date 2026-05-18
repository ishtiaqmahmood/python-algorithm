def soundex(name):
    """
    Calculates the Soundex code for a given name.

    Args:
        name (str): Input name.

    Returns:
        str: 4-character Soundex code.
    """
    if not name:
        return ""

    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }

    name = name.upper()
    code = name[0]
    last_digit = mapping.get(name[0], '0')

    for char in name[1:]:
        digit = mapping.get(char, '0')
        if digit != '0' and digit != last_digit:
            code += digit
        last_digit = digit
        if len(code) == 4:
            break

    return code.ljust(4, '0')


if __name__ == "__main__":
    for name in ["Washington", "Lee", "Jackson"]:
        print(f"Soundex of '{name}': {soundex(name)}")
