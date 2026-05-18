def motzkin_number(n):
    """
    Motzkin numbers M(n).
    M(n) = M(n-1) + sum_{i=0}^{n-2} M(i)M(n-2-i)
    """
    if n == 0 or n == 1: return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1]
        for j in range(i - 1):
            dp[i] += dp[j] * dp[i - 2 - j]
    return dp[n]


if __name__ == "__main__":
    for i in range(6):
        print(f"M({i}) = {motzkin_number(i)}")
