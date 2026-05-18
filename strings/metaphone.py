def metaphone(word):
    """
    Simplified Metaphone algorithm implementation.

    Args:
        word (str): Input word.

    Returns:
        str: Metaphone code.
    """
    word = word.upper()
    if not word:
        return ""

    # Basic rules (greatly simplified)
    res = []
    i = 0
    while i < len(word):
        c = word[i]
        if i == 0 and c in "AEIOU":
            res.append(c)
        elif c == 'B':
            if not (i == len(word) - 1 and word[i-1] == 'M'):
                res.append('B')
        elif c == 'C':
            if i + 1 < len(word) and word[i+1] in "IAH":
                res.append('X')
            elif i + 1 < len(word) and word[i+1] in "IEY":
                res.append('S')
            else:
                res.append('K')
        elif c == 'D':
            if i + 1 < len(word) and word[i+1] in "IEY":
                res.append('J')
            else:
                res.append('T')
        # ... more rules would be here in a full implementation
        else:
            if c not in "AEIOU":
                res.append(c)
        i += 1
    return "".join(res)


if __name__ == "__main__":
    print(f"Metaphone of 'Metaphone': {metaphone('Metaphone')}")
    print(f"Metaphone of 'Jackson': {metaphone('Jackson')}")
