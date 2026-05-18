class PushRelabel:
    """
    Push-Relabel algorithm for Maximum Flow.
    """
    def __init__(self, n):
        self.n = n
        self.graph = [[0] * n for _ in range(n)]
        self.h = [0] * n
        self.excess = [0] * n

    def add_edge(self, u, v, cap):
        self.graph[u][v] = cap

    def push(self, u, v):
        d = min(self.excess[u], self.graph[u][v])
        self.graph[u][v] -= d
        self.graph[v][u] += d
        self.excess[u] -= d
        self.excess[v] += d

    def relabel(self, u):
        min_h = float('inf')
        for v in range(self.n):
            if self.graph[u][v] > 0:
                min_h = min(min_h, self.h[v])
        if min_h != float('inf'):
            self.h[u] = min_h + 1

    def max_flow(self, s, t):
        self.h[s] = self.n
        self.excess[s] = float('inf')
        for v in range(self.n):
            if self.graph[s][v] > 0:
                self.push(s, v)

        while True:
            u = -1
            for i in range(self.n):
                if i != s and i != t and self.excess[i] > 0:
                    u = i; break
            if u == -1: break

            pushed = False
            for v in range(self.n):
                if self.graph[u][v] > 0 and self.h[u] == self.h[v] + 1:
                    self.push(u, v)
                    pushed = True; break
            if not pushed:
                self.relabel(u)
        return self.excess[t]


if __name__ == "__main__":
    pr = PushRelabel(6)
    pr.add_edge(0, 1, 16); pr.add_edge(0, 2, 13)
    pr.add_edge(1, 2, 10); pr.add_edge(1, 3, 12)
    pr.add_edge(2, 1, 4); pr.add_edge(2, 4, 14)
    pr.add_edge(3, 2, 9); pr.add_edge(3, 5, 20)
    pr.add_edge(4, 3, 7); pr.add_edge(4, 5, 4)
    print(f"Max Flow (Push-Relabel): {pr.max_flow(0, 5)}")
