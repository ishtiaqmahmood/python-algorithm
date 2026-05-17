def is_match(s, p):
    """
    Wildcard matching implementation.
    '?' matches any single character.
    '*' matches any sequence of characters.

    Args:
        s (str): The string.
        p (str): The pattern.

    Returns:
        bool: True if matches, False otherwise.
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][n]


if __name__ == "__main__":
    s, p = "adceb", "*a*b"
    print(f"Wildcard match ('{s}', '{p}'): {is_match(s, p)}")
