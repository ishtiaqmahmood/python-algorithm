def egg_dropping(n, k):
    """
    Finds the minimum number of trials needed to find the critical floor in the worst case.

    Args:
        n (int): Number of eggs.
        k (int): Number of floors.

    Returns:
        int: Minimum trials.
    """
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = 1
        dp[i][0] = 0

    for j in range(1, k + 1):
        dp[1][j] = j

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = float('inf')
            for x in range(1, j + 1):
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                if res < dp[i][j]:
                    dp[i][j] = res
    return dp[n][k]


if __name__ == "__main__":
    eggs = 2
    floors = 10
    print(f"Min trials for {eggs} eggs and {floors} floors: {egg_dropping(eggs, floors)}")
