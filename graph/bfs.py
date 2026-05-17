from collections import deque

def bfs(graph, start_node):
    """
    Breadth First Search traversal.

    Args:
        graph (dict): Adjacency list.
        start_node: Starting node.

    Returns:
        list: BFS traversal order.
    """
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
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
    print(f"BFS order: {bfs(test_graph, 'A')}")
