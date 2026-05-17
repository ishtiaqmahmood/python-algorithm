def coin_change(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount.

    Args:
        coins (list): List of coin denominations.
        amount (int): Target amount.

    Returns:
        int: Minimum number of coins, or -1 if it's not possible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    coin_list = [1, 2, 5]
    amt = 11
    print(f"Min coins for {amt} using {coin_list}: {coin_change(coin_list, amt)}")
