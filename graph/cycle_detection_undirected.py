def is_cyclic_undirected(num_nodes, adj):
    """
    Detects cycle in an undirected graph.

    Args:
        num_nodes (int): Number of nodes.
        adj (dict): Adjacency list.

    Returns:
        bool: True if cycle exists, False otherwise.
    """
    visited = [False] * num_nodes

    def dfs(u, parent):
        visited[u] = True
        for v in adj.get(u, []):
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for i in range(num_nodes):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


if __name__ == "__main__":
    g = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    print(f"Is undirected graph cyclic? {is_cyclic_undirected(4, g)}")
