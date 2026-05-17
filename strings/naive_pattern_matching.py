def naive_search(text, pattern):
    """
    Naive pattern matching algorithm.

    Args:
        text (str): Input text.
        pattern (str): Pattern to search.

    Returns:
        list: Starting indices of all matches.
    """
    n, m = len(text), len(pattern)
    result = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            result.append(i)
    return result


if __name__ == "__main__":
    t = "AABAACAADAABAAABAA"
    p = "AABA"
    print(f"Naive search matches at: {naive_search(t, p)}")
