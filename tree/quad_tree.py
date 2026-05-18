class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class QuadTreeNode:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.nw = self.ne = self.sw = self.se = None


class QuadTree:
    """
    Point QuadTree implementation.
    """
    def __init__(self):
        self.root = None

    def insert(self, x, y, val):
        if not self.root:
            self.root = QuadTreeNode(x, y, val)
            return
        self._insert(self.root, x, y, val)

    def _insert(self, node, x, y, val):
        if x < node.x:
            if y < node.y:
                if not node.sw: node.sw = QuadTreeNode(x, y, val)
                else: self._insert(node.sw, x, y, val)
            else:
                if not node.nw: node.nw = QuadTreeNode(x, y, val)
                else: self._insert(node.nw, x, y, val)
        else:
            if y < node.y:
                if not node.se: node.se = QuadTreeNode(x, y, val)
                else: self._insert(node.se, x, y, val)
            else:
                if not node.ne: node.ne = QuadTreeNode(x, y, val)
                else: self._insert(node.ne, x, y, val)


if __name__ == "__main__":
    qt = QuadTree()
    qt.insert(10, 10, "A")
    qt.insert(5, 5, "B")
    print("QuadTree point inserted.")
