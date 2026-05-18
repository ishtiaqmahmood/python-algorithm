class HLD:
    """
    Conceptual Heavy-Light Decomposition.
    """
    def __init__(self, adj):
        self.adj = adj
        self.n = len(adj)
        self.parent = [0] * self.n
        self.depth = [0] * self.n
        self.heavy = [-1] * self.n
        self.head = [0] * self.n
        self.pos = [0] * self.n
        self.cur_pos = 0
        self._dfs_sz(0)
        self._dfs_hld(0, 0)

    def _dfs_sz(self, u):
        size = 1
        max_c_size = 0
        for v in self.adj[u]:
            if v != self.parent[u]:
                self.parent[v] = u
                self.depth[v] = self.depth[u] + 1
                c_size = self._dfs_sz(v)
                size += c_size
                if c_size > max_c_size:
                    max_c_size = c_size
                    self.heavy[u] = v
        return size

    def _dfs_hld(self, u, h):
        self.head[u] = h
        self.pos[u] = self.cur_pos
        self.cur_pos += 1
        if self.heavy[u] != -1:
            self._dfs_hld(self.heavy[u], h)
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self._dfs_hld(v, v)


if __name__ == "__main__":
    adj = [[1, 2], [0, 3], [0], [1]]
    hld = HLD(adj)
    print("HLD initialized.")
