def count_partitions(n):
    """
    Counts the number of ways to write n as a sum of positive integers.
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n] + 1


if __name__ == "__main__":
    for i in range(1, 11):
        print(f"p({i}) = {count_partitions(i)}")
