class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


class NumArray:
    """
    Range Sum Query - Mutable using Fenwick Tree.
    """
    def __init__(self, nums):
        self.nums = nums
        self.ft = FenwickTree(len(nums))
        for i, v in enumerate(nums):
            self.ft.update(i, v)

    def update(self, index, val):
        self.ft.update(index, val - self.nums[index])
        self.nums[index] = val

    def sum_range(self, left, right):
        return self.ft.query(right) - self.ft.query(left - 1)


if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print(f"Sum(0, 2): {na.sum_range(0, 2)}")
    na.update(1, 2)
    print(f"Sum(0, 2): {na.sum_range(0, 2)}")
