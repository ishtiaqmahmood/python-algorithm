def graph_diameter(n, dist_matrix):
    """
    Calculates the diameter of a graph (maximum shortest path).
    """
    res = 0
    for i in range(n):
        for j in range(n):
            if dist_matrix[i][j] != float('inf'):
                res = max(res, dist_matrix[i][j])
    return res


if __name__ == "__main__":
    dist = [[0, 1, 2], [1, 0, 1], [2, 1, 0]]
    print(f"Graph Diameter: {graph_diameter(3, dist)}")
