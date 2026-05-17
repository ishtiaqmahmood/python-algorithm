def get_combinations(n, k):
    """
    Generates all combinations of k numbers from 1 to n.

    Args:
        n (int): Upper bound.
        k (int): Size of combination.

    Returns:
        list: List of combinations.
    """
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result


if __name__ == "__main__":
    print(f"Combinations (4, 2): {get_combinations(4, 2)}")
