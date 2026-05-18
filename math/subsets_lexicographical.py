def generate_subsets(n):
    """
    Generates all subsets of {1, ..., n} in lexicographical order.
    """
    res = [[]]
    for i in range(1, n + 1):
        new_subsets = []
        for s in res:
            new_subsets.append(s + [i])
        res.extend(new_subsets)
    return sorted(res)


if __name__ == "__main__":
    print(f"Subsets of 3: {generate_subsets(3)}")
