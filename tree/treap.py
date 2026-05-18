import random


class TreapNode:
    def __init__(self, val):
        self.val = val
        self.priority = random.random()
        self.left = None
        self.right = None


class Treap:
    """
    Treap (Tree + Heap) implementation.
    """
    def _split(self, node, val):
        if not node:
            return None, None
        if node.val < val:
            node.right, r = self._split(node.right, val)
            return node, r
        else:
            l, node.left = self._split(node.left, val)
            return l, node

    def _merge(self, l, r):
        if not l or not r:
            return l or r
        if l.priority > r.priority:
            l.right = self._merge(l.right, r)
            return l
        else:
            r.left = self._merge(l, r.left)
            return r

    def __init__(self):
        self.root = None

    def insert(self, val):
        l, r = self._split(self.root, val)
        self.root = self._merge(self._merge(l, TreapNode(val)), r)

    def search(self, val):
        curr = self.root
        while curr:
            if curr.val == val: return True
            curr = curr.right if curr.val < val else curr.left
        return False


if __name__ == "__main__":
    treap = Treap()
    treap.insert(10)
    treap.insert(20)
    treap.insert(5)
    print(f"Search 10: {treap.search(10)}")
    print(f"Search 15: {treap.search(15)}")
