import heapq


def a_star(graph, start, goal, h):
    """
    A* search algorithm.

    Args:
        graph (dict): Adjacency list with weights.
        start: Start node.
        goal: Goal node.
        h (dict): Heuristic values.

    Returns:
        list: Path from start to goal.
    """
    open_set = [(h[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))

    return None


if __name__ == "__main__":
    graph = {'A': {'B': 1, 'C': 3}, 'B': {'D': 1}, 'C': {'D': 1}, 'D': {}}
    h = {'A': 2, 'B': 1, 'C': 1, 'D': 0}
    print(f"A* Path: {a_star(graph, 'A', 'D', h)}")
