from collections import deque


class HopcroftKarp:
    """
    Hopcroft-Karp algorithm for maximum bipartite matching.
    """
    def __init__(self, nx, ny, adj):
        self.nx = nx
        self.ny = ny
        self.adj = adj
        self.pair_x = [-1] * nx
        self.pair_y = [-1] * ny
        self.dist = [0] * nx

    def bfs(self):
        queue = deque()
        for x in range(self.nx):
            if self.pair_x[x] == -1:
                self.dist[x] = 0
                queue.append(x)
            else:
                self.dist[x] = float("inf")

        found = False
        while queue:
            x = queue.popleft()
            for y in self.adj[x]:
                if self.pair_y[y] == -1:
                    found = True
                elif self.dist[self.pair_y[y]] == float("inf"):
                    self.dist[self.pair_y[y]] = self.dist[x] + 1
                    queue.append(self.pair_y[y])
        return found

    def dfs(self, x):
        for y in self.adj[x]:
            if self.pair_y[y] == -1 or (self.dist[self.pair_y[y]] == self.dist[x] + 1 and self.dfs(self.pair_y[y])):
                self.pair_x[x] = y
                self.pair_y[y] = x
                return True
        self.dist[x] = float("inf")
        return False

    def max_matching(self):
        matching = 0
        while self.bfs():
            for x in range(self.nx):
                if self.pair_x[x] == -1 and self.dfs(x):
                    matching += 1
        return matching


if __name__ == "__main__":
    adj = [[0, 1], [0], [1, 2]]
    hk = HopcroftKarp(3, 3, adj)
    print(f"Max Matching: {hk.max_matching()}")
