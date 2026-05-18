def longest_common_substring(s1, s2):
    """
    Finds the length of the longest common substring.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    res = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
    return res


if __name__ == "__main__":
    print(f"LCS length: {longest_common_substring('abcdef', 'zbcdf')}")
