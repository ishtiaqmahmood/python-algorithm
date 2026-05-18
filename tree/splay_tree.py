class SplayNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SplayTree:
    """
    Splay Tree implementation.
    """
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, val):
        if not root or root.val == val:
            return root

        if root.val > val:
            if not root.left: return root
            if root.left.val > val:
                root.left.left = self._splay(root.left.left, val)
                root = self._right_rotate(root)
            elif root.left.val < val:
                root.left.right = self._splay(root.left.right, val)
                if root.left.right:
                    root.left = self._left_rotate(root.left)
            return self._right_rotate(root) if root.left else root
        else:
            if not root.right: return root
            if root.right.val > val:
                root.right.left = self._splay(root.right.left, val)
                if root.right.left:
                    root.right = self._right_rotate(root.right)
            elif root.right.val < val:
                root.right.right = self._splay(root.right.right, val)
                root = self._left_rotate(root)
            return self._left_rotate(root) if root.right else root

    def search(self, val):
        self.root = self._splay(self.root, val)
        return self.root and self.root.val == val

    def insert(self, val):
        if not self.root:
            self.root = SplayNode(val)
            return
        self.root = self._splay(self.root, val)
        if self.root.val == val: return
        new_node = SplayNode(val)
        if self.root.val > val:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node


if __name__ == "__main__":
    st = SplayTree()
    st.insert(10)
    st.insert(20)
    st.insert(30)
    print(f"Search 10: {st.search(10)}")
    print(f"Root is now: {st.root.val}")
