class FordFulkerson:
    """
    Ford-Fulkerson algorithm for Maximum Flow.
    """
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)

    def dfs(self, s, t, parent, visited):
        visited[s] = True
        if s == t: return True
        for v, val in enumerate(self.graph[s]):
            if not visited[v] and val > 0:
                parent[v] = s
                if self.dfs(v, t, parent, visited):
                    return True
        return False

    def max_flow(self, source, sink):
        parent = [-1] * self.rows
        max_f = 0
        while True:
            visited = [False] * self.rows
            if not self.dfs(source, sink, parent, visited):
                break

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
    ff = FordFulkerson(graph)
    print(f"Max Flow: {ff.max_flow(0, 5)}")
