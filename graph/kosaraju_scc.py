def kosaraju_scc(num_nodes, adj):
    """
    Finds Strongly Connected Components using Kosaraju's algorithm.

    Args:
        num_nodes (int): Number of nodes.
        adj (dict): Adjacency list.

    Returns:
        list: List of SCCs.
    """
    stack = []
    visited = [False] * num_nodes

    def fill_order(u):
        visited[u] = True
        for v in adj.get(u, []):
            if not visited[v]:
                fill_order(v)
        stack.append(u)

    for i in range(num_nodes):
        if not visited[i]:
            fill_order(i)

    # Transpose graph
    adj_rev = {i: [] for i in range(num_nodes)}
    for u in adj:
        for v in adj[u]:
            adj_rev[v].append(u)

    visited = [False] * num_nodes
    sccs = []

    def dfs_rev(u, current_scc):
        visited[u] = True
        current_scc.append(u)
        for v in adj_rev.get(u, []):
            if not visited[v]:
                dfs_rev(v, current_scc)

    while stack:
        u = stack.pop()
        if not visited[u]:
            current_scc = []
            dfs_rev(u, current_scc)
            sccs.append(current_scc)
    return sccs


if __name__ == "__main__":
    g = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}
    print(f"SCCs (Kosaraju): {kosaraju_scc(5, g)}")
