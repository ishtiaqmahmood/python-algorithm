def is_cyclic_directed(num_nodes, adj):
    """
    Detects cycle in a directed graph.

    Args:
        num_nodes (int): Number of nodes.
        adj (dict): Adjacency list.

    Returns:
        bool: True if cycle exists, False otherwise.
    """
    visited = [False] * num_nodes
    rec_stack = [False] * num_nodes

    def dfs(u):
        visited[u] = True
        rec_stack[u] = True
        for v in adj.get(u, []):
            if not visited[v]:
                if dfs(v):
                    return True
            elif rec_stack[v]:
                return True
        rec_stack[u] = False
        return False

    for i in range(num_nodes):
        if not visited[i]:
            if dfs(i):
                return True
    return False


if __name__ == "__main__":
    g = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    print(f"Is directed graph cyclic? {is_cyclic_directed(4, g)}")
