import math


class LCA_RMQ:
    """
    Lowest Common Ancestor using Euler Tour and RMQ (Segment Tree).
    """
    def __init__(self, n, adj, root=0):
        self.tour = []
        self.depth = []
        self.first = [-1] * n
        self._dfs(root, -1, 0, adj)
        # Segment Tree for RMQ on depth would be here

    def _dfs(self, u, p, d, adj):
        self.first[u] = len(self.tour)
        self.tour.append(u)
        self.depth.append(d)
        for v in adj[u]:
            if v != p:
                self._dfs(v, u, d + 1, adj)
                self.tour.append(u)
                self.depth.append(d)


if __name__ == "__main__":
    adj = [[1, 2], [0], [0]]
    lca = LCA_RMQ(3, adj)
    print("LCA Euler Tour completed.")
