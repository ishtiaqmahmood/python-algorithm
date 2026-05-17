def kmp_search(text, pattern):
    """
    Implementation of Knuth-Morris-Pratt pattern matching algorithm.

    Args:
        text (str): The string to search in.
        pattern (str): The pattern to search for.

    Returns:
        list: Starting indices of all matches.
    """
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    # Compute LPS array
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    # Search
    result = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            result.append(i - m + 1)
            j = lps[j - 1]

    return result


if __name__ == "__main__":
    t = "ABABDABACDABABCABAB"
    p = "ABABCABAB"
    print(f"KMP Search matches at: {kmp_search(t, p)}")
