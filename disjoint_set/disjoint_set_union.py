class DSU:
    """
    Implementation of Disjoint Set Union (DSU) / Union-Find.
    """
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

if __name__ == "__main__":
    dsu = DSU(5)
    dsu.union(0, 2)
    dsu.union(4, 2)
    dsu.union(3, 1)
    print(f"0 and 4 connected: {dsu.find(0) == dsu.find(4)}")
    print(f"0 and 1 connected: {dsu.find(0) == dsu.find(1)}")
