def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(graph, m):
    """
    Solves the m-Coloring problem.

    Args:
        graph (list): 2D adjacency matrix.
        m (int): Number of colors.

    Returns:
        list: Color assigned to each vertex, or None.
    """
    n = len(graph)
    color = [0] * n

    def backtrack(v):
        if v == n:
            return True

        for c in range(1, m + 1):
            if is_safe(v, graph, color, c):
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = 0
        return False

    if backtrack(0):
        return color
    return None


if __name__ == "__main__":
    test_graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    num_colors = 3
    print(f"Graph coloring with {num_colors} colors: {graph_coloring(test_graph, num_colors)}")
