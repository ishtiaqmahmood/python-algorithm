from collections import deque


class EdmondsKarp:
    """
    Edmonds-Karp algorithm for Maximum Flow (BFS-based Ford-Fulkerson).
    """
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.n
        queue = deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v, val in enumerate(self.graph[u]):
                if not visited[v] and val > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t: return True
        return False

    def max_flow(self, source, sink):
        parent = [-1] * self.n
        max_f = 0
        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_f += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_f


if __name__ == "__main__":
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]
    ek = EdmondsKarp(graph)
    print(f"Max Flow (EK): {ek.max_flow(0, 5)}")
