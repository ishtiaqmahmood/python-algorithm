def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem.

    Args:
        weights (list): List of weights of items.
        values (list): List of values of items.
        capacity (int): Maximum capacity of the knapsack.

    Returns:
        int: Maximum value that can be obtained.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


if __name__ == "__main__":
    wts = [1, 3, 4, 5]
    vals = [1, 4, 5, 7]
    cap = 7
    print(f"Max value in 0/1 Knapsack (cap={cap}): {knapsack_01(wts, vals, cap)}")
