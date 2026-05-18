from collections import deque


def min_cut(graph, s, t):
    """
    Finds the minimum cut in a flow network.

    Args:
        graph (list): Residual graph.
        s (int): Source.
        t (int): Sink.

    Returns:
        list: Edges that form the min-cut.
    """
    n = len(graph)
    residual = [row[:] for row in graph]

    # Edmonds-Karp to get residual graph
    def bfs(residual, s, t, parent):
        visited = [False] * n
        queue = deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v, cap in enumerate(residual[u]):
                if not visited[v] and cap > 0:
                    parent[v] = u
                    visited[v] = True
                    queue.append(v)
                    if v == t: return True
        return False

    parent = [-1] * n
    while bfs(residual, s, t, parent):
        path_flow = float("inf")
        curr = t
        while curr != s:
            path_flow = min(path_flow, residual[parent[curr]][curr])
            curr = parent[curr]
        curr = t
        while curr != s:
            u = parent[curr]
            residual[u][curr] -= path_flow
            residual[curr][u] += path_flow
            curr = parent[curr]

    # Find reachable nodes from s in residual graph
    visited = [False] * n
    queue = deque([s])
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v, cap in enumerate(residual[u]):
            if not visited[v] and cap > 0:
                visited[v] = True
                queue.append(v)

    cuts = []
    for i in range(n):
        for j in range(n):
            if visited[i] and not visited[j] and graph[i][j] > 0:
                cuts.append((i, j))
    return cuts


if __name__ == "__main__":
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]
    print(f"Min Cut Edges: {min_cut(graph, 0, 5)}")
