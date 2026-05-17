def bellman_ford(num_nodes, edges, start_node):
    """
    Bellman-Ford algorithm for shortest paths.

    Args:
        num_nodes (int): Number of nodes.
        edges (list): List of (u, v, weight) tuples.
        start_node (int): Starting node.

    Returns:
        list: Shortest distances from start_node.
    """
    dist = [float('inf')] * num_nodes
    dist[start_node] = 0

    for _ in range(num_nodes - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return None

    return dist


if __name__ == "__main__":
    e = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
    print(f"Bellman-Ford distances: {bellman_ford(5, e, 0)}")
