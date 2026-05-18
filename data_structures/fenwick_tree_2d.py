class FenwickTree2D:
    def __init__(self, rows, cols):
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def update(self, r, c, delta):
        i = r + 1
        while i < len(self.tree):
            j = c + 1
            while j < len(self.tree[0]):
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def query(self, r, c):
        i, s = r + 1, 0
        while i > 0:
            j = c + 1
            while j > 0:
                s += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return s


if __name__ == "__main__":
    ft = FenwickTree2D(3, 3)
    ft.update(1, 1, 5)
    print(f"Query(1, 1): {ft.query(1, 1)}")
