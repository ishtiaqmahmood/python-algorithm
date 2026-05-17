def dfs(graph, start_node):
    """
    Depth First Search traversal.

    Args:
        graph (dict): Adjacency list.
        start_node: Starting node.

    Returns:
        list: DFS traversal order.
    """
    visited = set()
    result = []

    def traverse(u):
        visited.add(u)
        result.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                traverse(v)

    traverse(start_node)
    return result


if __name__ == "__main__":
    test_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print(f"DFS order: {dfs(test_graph, 'A')}")
