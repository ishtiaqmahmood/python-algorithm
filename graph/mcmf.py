import heapq


class MCMF:
    """
    Min-Cost Max-Flow algorithm using successive shortest path with SPFA or Dijkstra.
    """
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, cost):
        self.graph[u].append([v, cap, cost, len(self.graph[v])])
        self.graph[v].append([u, 0, -cost, len(self.graph[u]) - 1])

    def spfa(self, s, t, dist, parent, edge_from):
        dist[:] = [float('inf')] * self.n
        dist[s] = 0
        in_queue = [False] * self.n
        queue = [s]
        in_queue[s] = True

        while queue:
            u = queue.pop(0)
            in_queue[u] = False
            for i, (v, cap, cost, rev) in enumerate(self.graph[u]):
                if cap > 0 and dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    parent[v] = u
                    edge_from[v] = i
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True
        return dist[t] != float('inf')

    def min_cost_max_flow(self, s, t):
        dist = [0] * self.n
        parent = [-1] * self.n
        edge_from = [-1] * self.n
        max_flow = 0
        min_cost = 0
        while self.spfa(s, t, dist, parent, edge_from):
            flow = float('inf')
            curr = t
            while curr != s:
                u = parent[curr]
                idx = edge_from[curr]
                flow = min(flow, self.graph[u][idx][1])
                curr = u

            max_flow += flow
            curr = t
            while curr != s:
                u = parent[curr]
                idx = edge_from[curr]
                rev_idx = self.graph[u][idx][3]
                self.graph[u][idx][1] -= flow
                self.graph[curr][rev_idx][1] += flow
                min_cost += flow * self.graph[u][idx][2]
                curr = u
        return max_flow, min_cost


if __name__ == "__main__":
    mcmf = MCMF(4)
    mcmf.add_edge(0, 1, 1, 1)
    mcmf.add_edge(0, 2, 1, 2)
    mcmf.add_edge(1, 3, 1, 2)
    mcmf.add_edge(2, 3, 1, 1)
    print(f"Max Flow, Min Cost: {mcmf.min_cost_max_flow(0, 3)}")
