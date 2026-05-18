def palindrome_partition_iii(s, k):
    """
    Palindrome Partitioning III (Minimum changes).
    """
    n = len(s)

    # Precompute changes needed to make s[i:j+1] a palindrome
    changes = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            changes[i][j] = changes[i+1][j-1] + (1 if s[i] != s[j] else 0)

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][1] = changes[0][i-1]
        for j in range(2, min(i, k) + 1):
            for p in range(j - 1, i):
                dp[i][j] = min(dp[i][j], dp[p][j-1] + changes[p][i-1])

    return dp[n][k]


if __name__ == "__main__":
    print(f"Min changes (abc, k=2): {palindrome_partition_iii('abc', 2)}")
