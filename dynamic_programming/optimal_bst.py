def optimal_bst(freq):
    """
    Optimal Binary Search Tree problem.

    Args:
        freq (list): Frequencies of keys.

    Returns:
        int: Minimum search cost.
    """
    n = len(freq)
    cost = [[0] * n for _ in range(n)]
    for i in range(n): cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            off_set_sum = sum(freq[i:j+1])
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                c = (cost[i][r-1] if r > i else 0) + (cost[r+1][j] if r < j else 0) + off_set_sum
                cost[i][j] = min(cost[i][j], c)
    return cost[0][n-1]


if __name__ == "__main__":
    freq = [34, 8, 50]
    print(f"Min search cost: {optimal_bst(freq)}")
