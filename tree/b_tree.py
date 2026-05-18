class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    """
    Simplified B-Tree implementation.
    """
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree

    def search(self, k, x=None):
        if x is None: x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return True
        if x.leaf:
            return False
        return self.search(k, x.child[i])


if __name__ == "__main__":
    bt = BTree(3)
    print("B-Tree initialized.")
