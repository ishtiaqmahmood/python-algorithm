class CentroidDecomposition:
    """
    Centroid Decomposition of a tree.
    """
    def __init__(self, adj):
        self.adj = adj
        self.n = len(adj)
        self.sz = [0] * self.n
        self.is_removed = [False] * self.n

    def get_size(self, u, p):
        self.sz[u] = 1
        for v in self.adj[u]:
            if v != p and not self.is_removed[v]:
                self.sz[u] += self.get_size(v, u)
        return self.sz[u]

    def find_centroid(self, u, p, n):
        for v in self.adj[u]:
            if v != p and not self.is_removed[v]:
                if self.sz[v] > n // 2:
                    return self.find_centroid(v, u, n)
        return u

    def decompose(self, u):
        centroid = self.find_centroid(u, -1, self.get_size(u, -1))
        self.is_removed[centroid] = True
        for v in self.adj[centroid]:
            if not self.is_removed[v]:
                self.decompose(v)


if __name__ == "__main__":
    adj = [[1], [0, 2, 3], [1], [1]]
    cd = CentroidDecomposition(adj)
    cd.decompose(0)
    print("Centroid Decomposition completed.")
