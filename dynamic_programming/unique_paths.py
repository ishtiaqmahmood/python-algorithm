def unique_paths(m, n):
    """
    Finds the number of unique paths from top-left to bottom-right of an m x n grid.
    Only down and right moves are allowed.

    Args:
        m (int): Number of rows.
        n (int): Number of columns.

    Returns:
        int: Number of unique paths.
    """
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(f"Unique paths for 3x7 grid: {unique_paths(3, 7)}")
