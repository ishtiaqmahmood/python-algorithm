def racecar(target):
    """
    Race Car (BFS or DP).
    """
    dp = {0: 0}

    def solve(t):
        if t in dp: return dp[t]
        n = t.bit_length()
        if (1 << n) - 1 == t:
            dp[t] = n
        else:
            # Case 1: Pass target and reverse
            dp[t] = n + 1 + solve((1 << n) - 1 - t)
            # Case 2: Stop before target and reverse
            for m in range(n - 1):
                dp[t] = min(dp[t], n - 1 + 1 + m + 1 + solve(t - ((1 << (n - 1)) - 1) + ((1 << m) - 1)))
        return dp[t]

    return solve(target)


if __name__ == "__main__":
    print(f"Racecar steps for 3: {racecar(3)}")
    print(f"Racecar steps for 6: {racecar(6)}")
