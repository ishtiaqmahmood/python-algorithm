class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []
        self.next = None


class BPlusTree:
    """
    Simplified B+ Tree implementation.
    """
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t

if __name__ == "__main__":
    bpt = BPlusTree(3)
    print("B+ Tree initialized.")
