def num_rolls_to_target(n, k, target):
    """
    Number of Dice Rolls With Target Sum.
    """
    mod = 10**9 + 7
    dp = [0] * (target + 1)
    dp[0] = 1
    for _ in range(n):
        new_dp = [0] * (target + 1)
        for i in range(1, k + 1):
            for j in range(i, target + 1):
                new_dp[j] = (new_dp[j] + dp[j-i]) % mod
        dp = new_dp
    return dp[target]


if __name__ == "__main__":
    print(f"Dice rolls for target 7: {num_rolls_to_target(2, 6, 7)}")
