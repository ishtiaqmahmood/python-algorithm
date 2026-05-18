class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = self.mid = self.right = None
        self.is_end = False


class TernarySearchTree:
    """
    Ternary Search Tree (TST) implementation.
    """
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, i):
        char = word[i]
        if not node:
            node = TSTNode(char)

        if char < node.char:
            node.left = self._insert(node.left, word, i)
        elif char > node.char:
            node.right = self._insert(node.right, word, i)
        elif i < len(word) - 1:
            node.mid = self._insert(node.mid, word, i + 1)
        else:
            node.is_end = True
        return node

    def search(self, word):
        node = self._search(self.root, word, 0)
        return node is not None and node.is_end

    def _search(self, node, word, i):
        if not node: return None
        char = word[i]
        if char < node.char:
            return self._search(node.left, word, i)
        elif char > node.char:
            return self._search(node.right, word, i)
        elif i < len(word) - 1:
            return self._search(node.mid, word, i + 1)
        else:
            return node


if __name__ == "__main__":
    tst = TernarySearchTree()
    tst.insert("cat")
    tst.insert("bug")
    print(f"Search 'cat': {tst.search('cat')}")
    print(f"Search 'dog': {tst.search('dog')}")
