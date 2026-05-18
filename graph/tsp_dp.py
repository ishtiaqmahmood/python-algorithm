def tsp_dp(dist):
    """
    Traveling Salesperson Problem using Dynamic Programming (Held-Karp).

    Args:
        dist (list): 2D distance matrix.

    Returns:
        int: Minimum cost.
    """
    n = len(dist)
    memo = {}

    def solve(mask, last):
        if mask == (1 << n) - 1:
            return dist[last][0]
        if (mask, last) in memo:
            return memo[(mask, last)]

        res = float('inf')
        for next_node in range(n):
            if not (mask & (1 << next_node)):
                res = min(res, dist[last][next_node] + solve(mask | (1 << next_node), next_node))

        memo[(mask, last)] = res
        return res

    return solve(1, 0)


if __name__ == "__main__":
    dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print(f"Min TSP Cost: {tsp_dp(dist)}")
