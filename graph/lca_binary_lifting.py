import math


class LCA:
    """
    Lowest Common Ancestor using Binary Lifting.
    """
    def __init__(self, n, adj, root=0):
        self.n = n
        self.log = int(math.log2(n)) + 1
        self.up = [[-1] * self.log for _ in range(n)]
        self.tin = [0] * n
        self.tout = [0] * n
        self.timer = 0
        self._dfs(root, -1, adj)

    def _dfs(self, u, p, adj):
        self.timer += 1
        self.tin[u] = self.timer
        self.up[u][0] = p
        for i in range(1, self.log):
            if self.up[u][i-1] != -1:
                self.up[u][i] = self.up[self.up[u][i-1]][i-1]
        for v in adj[u]:
            if v != p:
                self._dfs(v, u, adj)
        self.tout[u] = self.timer

    def is_ancestor(self, u, v):
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def query(self, u, v):
        if self.is_ancestor(u, v): return u
        if self.is_ancestor(v, u): return v
        for i in range(self.log - 1, -1, -1):
            if self.up[u][i] != -1 and not self.is_ancestor(self.up[u][i], v):
                u = self.up[u][i]
        return self.up[u][0]


if __name__ == "__main__":
    adj = [[1, 2], [0, 3, 4], [0], [1], [1]]
    lca = LCA(5, adj)
    print(f"LCA of 3 and 4: {lca.query(3, 4)}")
