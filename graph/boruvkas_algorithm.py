class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_sets -= 1
            return True
        return False


def boruvka(n, edges):
    """
    Boruvka's algorithm for Minimum Spanning Tree.

    Args:
        n (int): Number of vertices.
        edges (list): List of (u, v, w).

    Returns:
        int: Total MST weight.
    """
    dsu = DSU(n)
    mst_weight = 0
    while dsu.num_sets > 1:
        cheapest = [-1] * n
        for i, (u, v, w) in enumerate(edges):
            root_u, root_v = dsu.find(u), dsu.find(v)
            if root_u != root_v:
                if cheapest[root_u] == -1 or edges[cheapest[root_u]][2] > w:
                    cheapest[root_u] = i
                if cheapest[root_v] == -1 or edges[cheapest[root_v]][2] > w:
                    cheapest[root_v] = i

        added = False
        for i in range(n):
            if cheapest[i] != -1:
                u, v, w = edges[cheapest[i]]
                if dsu.union(u, v):
                    mst_weight += w
                    added = True
        if not added: break
    return mst_weight


if __name__ == "__main__":
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    print(f"MST Weight (Boruvka): {boruvka(4, edges)}")
