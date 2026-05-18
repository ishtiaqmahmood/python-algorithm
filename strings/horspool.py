def horspool_search(text, pattern):
    """
    Horspool's string searching algorithm.

    Args:
        text (str): Text to search in.
        pattern (str): Pattern to search for.

    Returns:
        int: Index of first occurrence, or -1.
    """
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    skip = {char: m for char in text}
    for i in range(m - 1):
        skip[pattern[i]] = m - 1 - i

    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        i += skip.get(text[i], m)
    return -1


if __name__ == "__main__":
    text = "this is a test string"
    pattern = "test"
    print(f"Index of '{pattern}' in '{text}': {horspool_search(text, pattern)}")
