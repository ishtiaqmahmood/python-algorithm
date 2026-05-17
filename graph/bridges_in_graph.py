def find_bridges(num_nodes, adj):
    """
    Finds all bridges in an undirected graph using Tarjan's algorithm idea.

    Args:
        num_nodes (int): Number of nodes.
        adj (dict): Adjacency list.

    Returns:
        list: List of bridges (u, v).
    """
    timer = 0
    tin = [-1] * num_nodes
    low = [-1] * num_nodes
    bridges = []

    def dfs(u, p=-1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v in adj.get(u, []):
            if v == p: continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.append((u, v))

    for i in range(num_nodes):
        if tin[i] == -1:
            dfs(i)
    return bridges


if __name__ == "__main__":
    g = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    print(f"Bridges: {find_bridges(4, g)}")
