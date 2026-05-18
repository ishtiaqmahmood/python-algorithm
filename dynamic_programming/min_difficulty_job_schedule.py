def min_difficulty(job_difficulty, d):
    """
    Minimum Difficulty of a Job Schedule.
    """
    n = len(job_difficulty)
    if n < d: return -1

    dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for k in range(1, min(i, d) + 1):
            cur_max = 0
            for j in range(i - 1, k - 2, -1):
                cur_max = max(cur_max, job_difficulty[j])
                dp[i][k] = min(dp[i][k], dp[j][k-1] + cur_max)
    return dp[n][d]


if __name__ == "__main__":
    print(f"Min difficulty: {min_difficulty([6, 5, 4, 3, 2, 1], 2)}")
