def fractional_knapsack(weights, values, capacity):
    """
    Solves the Fractional Knapsack problem using a greedy approach.

    Args:
        weights (list): Weights of items.
        values (list): Values of items.
        capacity (int): Max capacity of knapsack.

    Returns:
        float: Maximum value.
    """
    items = []
    for i in range(len(weights)):
        items.append((values[i], weights[i], values[i] / weights[i]))

    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    for value, weight, ratio in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break
    return total_value


if __name__ == "__main__":
    wts = [10, 20, 30]
    vals = [60, 100, 120]
    cap = 50
    print(f"Max value in Fractional Knapsack: {fractional_knapsack(wts, vals, cap)}")
