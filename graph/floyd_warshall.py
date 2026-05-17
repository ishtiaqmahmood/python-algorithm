def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for all-pairs shortest paths.

    Args:
        graph (list): 2D adjacency matrix (dist[i][j] = weight or inf).

    Returns:
        list: 2D matrix of shortest paths.
    """
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == "__main__":
    inf = float('inf')
    test_graph = [
        [0, 5, inf, 10],
        [inf, 0, 3, inf],
        [inf, inf, 0, 1],
        [inf, inf, inf, 0]
    ]
    print("Floyd-Warshall distances:")
    for row in floyd_warshall(test_graph):
        print(row)
