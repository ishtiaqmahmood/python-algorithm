import math


class SparseTable:
    """
    Sparse Table for Range Minimum Query.
    """
    def __init__(self, arr):
        n = len(arr)
        k = int(math.log2(n)) + 1
        self.st = [[0] * k for _ in range(n)]
        for i in range(n): self.st[i][0] = arr[i]

        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = min(self.st[i][j-1], self.st[i + (1 << (j-1))][j-1])

    def query(self, l, r):
        j = int(math.log2(r - l + 1))
        return min(self.st[l][j], self.st[r - (1 << j) + 1][j])


if __name__ == "__main__":
    st = SparseTable([7, 2, 3, 0, 5, 10, 3, 12, 18])
    print(f"RMQ(0, 4): {st.query(0, 4)}")
