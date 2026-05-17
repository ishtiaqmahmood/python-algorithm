def kruskals_algorithm(num_nodes, edges):
    """
    Finds the Minimum Spanning Tree using Kruskal's algorithm.

    Args:
        num_nodes (int): Number of nodes.
        edges (list): List of tuples (u, v, weight).

    Returns:
        list: Edges in the MST.
    """
    edges.sort(key=lambda x: x[2])
    parent = list(range(num_nodes))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    mst = []
    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
    return mst


if __name__ == "__main__":
    node_count = 4
    edge_list = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    print(f"MST Edges (Kruskal's): {kruskals_algorithm(node_count, edge_list)}")
