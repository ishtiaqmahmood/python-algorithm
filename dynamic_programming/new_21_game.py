def new_21_game(n, k, max_pts):
    """
    New 21 Game probability.
    """
    if k == 0 or n >= k + max_pts: return 1.0
    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    window_sum = 1.0
    for i in range(1, n + 1):
        dp[i] = window_sum / max_pts
        if i < k: window_sum += dp[i]
        if i >= max_pts: window_sum -= dp[i - max_pts]
    return sum(dp[k:])


if __name__ == "__main__":
    print(f"Prob (n=10, k=1, max=10): {new_21_game(10, 1, 10)}")
