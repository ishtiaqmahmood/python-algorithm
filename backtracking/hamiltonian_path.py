def hamiltonian_path(graph):
    """
    Finds a Hamiltonian Path in a graph.

    Args:
        graph (list): 2D adjacency matrix.

    Returns:
        list: Hamiltonian path as a sequence of vertices.
    """
    n = len(graph)
    path = []
    visited = [False] * n

    def backtrack(u):
        path.append(u)
        visited[u] = True
        if len(path) == n:
            return True

        for v in range(n):
            if graph[u][v] == 1 and not visited[v]:
                if backtrack(v):
                    return True

        visited[u] = False
        path.pop()
        return False

    for i in range(n):
        if backtrack(i):
            return path
    return None


if __name__ == "__main__":
    test_graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]
    print(f"Hamiltonian Path: {hamiltonian_path(test_graph)}")
