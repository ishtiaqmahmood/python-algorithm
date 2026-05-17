def rod_cutting(prices, n):
    """
    Determines the maximum value obtainable by cutting up the rod and selling the pieces.

    Args:
        prices (list): prices[i] is the price of a rod of length i+1.
        n (int): Length of the rod.

    Returns:
        int: Maximum obtainable value.
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, prices[j] + dp[i - j - 1])
        dp[i] = max_val
    return dp[n]


if __name__ == "__main__":
    rod_prices = [1, 5, 8, 9, 10, 17, 17, 20]
    length = 8
    print(f"Max value for rod length {length}: {rod_cutting(rod_prices, length)}")
