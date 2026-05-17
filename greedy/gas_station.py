def can_complete_circuit(gas, cost):
    """
    Solves the Gas Station problem.

    Args:
        gas (list): Gas available at each station.
        cost (list): Cost to travel to the next station.

    Returns:
        int: Starting gas station index, or -1.
    """
    if sum(gas) < sum(cost):
        return -1

    total_gas = 0
    start_index = 0
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        if total_gas < 0:
            total_gas = 0
            start_index = i + 1

    return start_index


if __name__ == "__main__":
    g = [1, 2, 3, 4, 5]
    c = [3, 4, 5, 1, 2]
    print(f"Starting gas station index: {can_complete_circuit(g, c)}")
