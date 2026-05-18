def max_profit(prices):
    """
    Best Time to Buy and Sell Stock II (Multiple transactions).
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


if __name__ == "__main__":
    print(f"Max profit (any txn): {max_profit([7, 1, 5, 3, 6, 4])}")
