def is_interleave(s1, s2, s3):
    """
    Interleaving String using DP.
    """
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [False] * (len(s2) + 1)
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
            elif j == 0:
                dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
            else:
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
    return dp[len(s2)]


if __name__ == "__main__":
    print(f"Is interleave? {is_interleave('aabcc', 'dbbca', 'aadbbcbcac')}")
