class SegmentTree:
    """
    Implementation of a Segment Tree for Range Sum Queries.
    """
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node + 1, start, mid)
        self._build(data, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, idx, val):
        """Updates the value at idx to val."""
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self._update(2 * node + 1, start, mid, idx, val)
        else:
            self._update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r):
        """Returns the sum in range [l, r]."""
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node + 1, start, mid, l, r)
        p2 = self._query(2 * node + 2, mid + 1, end, l, r)
        return p1 + p2

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print(f"Sum in range [1, 3]: {st.query(1, 3)}")
    st.update(1, 10)
    print(f"Sum in range [1, 3] after update: {st.query(1, 3)}")
