def is_interleave(s1, s2, s3):
    """
    Checks if s3 is formed by interleaving s1 and s2.

    Args:
        s1 (str): First string.
        s2 (str): Second string.
        s3 (str): Third string.

    Returns:
        bool: True if s3 is interleaved, False otherwise.
    """
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0:
                dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            if j > 0:
                dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
    print(f"Is '{s3}' interleaved by '{s1}' and '{s2}'? {is_interleave(s1, s2, s3)}")
