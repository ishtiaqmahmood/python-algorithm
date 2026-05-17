def compress(chars):
    """
    Compresses a list of characters by replacing consecutive duplicates with the character followed by the count.

    Args:
        chars (list): List of characters.

    Returns:
        str: Compressed string.
    """
    if not chars:
        return ""
    res = []
    i = 0
    while i < len(chars):
        char = chars[i]
        count = 0
        while i < len(chars) and chars[i] == char:
            count += 1
            i += 1
        res.append(char)
        if count > 1:
            res.append(str(count))
    return "".join(res)


if __name__ == "__main__":
    test_chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(f"Compressed {test_chars}: {compress(test_chars)}")
