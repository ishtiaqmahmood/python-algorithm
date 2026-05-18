def generate_combinations(n, k):
    """
    Generates all k-combinations of {1, ..., n} in lexicographical order.
    """
    res = []
    def backtrack(start, curr):
        if len(curr) == k:
            res.append(list(curr))
            return
        for i in range(start, n + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()

    backtrack(1, [])
    return res


if __name__ == "__main__":
    print(f"Combinations(4, 2): {generate_combinations(4, 2)}")
