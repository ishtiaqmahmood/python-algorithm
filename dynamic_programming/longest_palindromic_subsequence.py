def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence in a string.

    Args:
        s (str): The input string.

    Returns:
        int: Length of the longest palindromic subsequence.
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


if __name__ == "__main__":
    test_str = "bbbab"
    print(f"Longest palindromic subsequence length of '{test_str}': {longest_palindromic_subsequence(test_str)}")
