def super_egg_drop(k, n):
    """
    Super Egg Drop.
    """
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    m = 0
    while dp[m][k] < n:
        m += 1
        for i in range(1, k + 1):
            dp[m][i] = dp[m-1][i-1] + dp[m-1][i] + 1
    return m


if __name__ == "__main__":
    print(f"Min moves (k=2, n=6): {super_egg_drop(2, 6)}")
