def max_profit(prices):
    """
    Best Time to Buy and Sell Stock I (One transaction).
    """
    min_price = float('inf')
    max_p = 0
    for price in prices:
        min_price = min(min_price, price)
        max_p = max(max_p, price - min_price)
    return max_p


if __name__ == "__main__":
    print(f"Max profit (1 txn): {max_profit([7, 1, 5, 3, 6, 4])}")
