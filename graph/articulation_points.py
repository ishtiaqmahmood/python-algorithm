def find_articulation_points(num_nodes, adj):
    """
    Finds articulation points in an undirected graph.

    Args:
        num_nodes (int): Number of nodes.
        adj (dict): Adjacency list.

    Returns:
        set: Articulation points.
    """
    timer = 0
    tin = [-1] * num_nodes
    low = [-1] * num_nodes
    is_ap = [False] * num_nodes

    def dfs(u, p=-1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        children = 0
        for v in adj.get(u, []):
            if v == p: continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] >= tin[u] and p != -1:
                    is_ap[u] = True
                children += 1
        return children

    for i in range(num_nodes):
        if tin[i] == -1:
            if dfs(i) > 1:
                is_ap[i] = True

    return {i for i, val in enumerate(is_ap) if val}


if __name__ == "__main__":
    g = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    print(f"Articulation Points: {find_articulation_points(4, g)}")
