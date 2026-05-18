def min_palindromic_cuts(s):
    """
    Palindrome Partitioning II (Minimum cuts).

    Args:
        s (str): Input string.

    Returns:
        int: Minimum cuts.
    """
    n = len(s)
    cuts = list(range(n))
    is_pal = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if s[i] == s[j] and (i - j < 2 or is_pal[j + 1][i - 1]):
                is_pal[j][i] = True
                cuts[i] = 0 if j == 0 else min(cuts[i], cuts[j - 1] + 1)
    return cuts[n - 1]


if __name__ == "__main__":
    s = "aab"
    print(f"Min cuts for '{s}': {min_palindromic_cuts(s)}")
