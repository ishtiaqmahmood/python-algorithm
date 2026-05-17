def edit_distance(s1, s2):
    """
    Computes the minimum number of operations to convert s1 to s2.
    Operations: Insertion, Deletion, Substitution.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        int: Minimum edit distance.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                   dp[i][j - 1],      # Insertion
                                   dp[i - 1][j - 1]) # Substitution
    return dp[m][n]


if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    print(f"Edit distance between '{str1}' and '{str2}': {edit_distance(str1, str2)}")
