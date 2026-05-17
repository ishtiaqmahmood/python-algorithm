class FenwickTree:
    """
    Implementation of Fenwick Tree (Binary Indexed Tree) for Range Sum Queries.
    """
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        """Adds delta to element at index i (1-indexed)."""
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        """Returns the prefix sum up to index i (1-indexed)."""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_query(self, l, r):
        """Returns the sum in range [l, r] (1-indexed)."""
        return self.query(r) - self.query(l - 1)

if __name__ == "__main__":
    arr = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
    ft = FenwickTree(len(arr))
    for i, val in enumerate(arr):
        ft.update(i + 1, val)
    print(f"Sum of first 5 elements: {ft.query(5)}")
    print(f"Sum of elements from index 2 to 5: {ft.range_query(2, 5)}")
