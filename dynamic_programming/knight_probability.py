def knight_probability(n, k, r, c):
    """
    Knight Probability in Chessboard.
    """
    dp = [[0] * n for _ in range(n)]
    dp[r][c] = 1
    for _ in range(k):
        new_dp = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if dp[r][c] > 0:
                    for dr, dc in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += dp[r][c] / 8.0
        dp = new_dp
    return sum(map(sum, dp))


if __name__ == "__main__":
    print(f"Knight probability: {knight_probability(3, 2, 0, 0)}")
