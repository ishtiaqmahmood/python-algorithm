def max_independent_set(adj):
    """
    Finds a maximum independent set in a graph (conceptual/heuristic for NP-hard).
    """
    # Using a simple greedy heuristic
    nodes = sorted(adj.keys(), key=lambda x: len(adj[x]))
    independent_set = []
    removed = set()
    for node in nodes:
        if node not in removed:
            independent_set.append(node)
            removed.add(node)
            removed.update(adj[node])
    return independent_set


if __name__ == "__main__":
    adj = {0: {1, 2}, 1: {0, 2}, 2: {0, 1, 3}, 3: {2}}
    print(f"Independent Set (Greedy): {max_independent_set(adj)}")
