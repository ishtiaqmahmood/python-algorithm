class SuffixTreeNode:
    def __init__(self, start=-1, end=None):
        self.children = {}
        self.start = start
        self.end = end
        self.suffix_link = None

class SuffixTree:
    """
    Suffix Tree (Ukkonen's Algorithm - simplified version or conceptual).
    """
    def __init__(self, s):
        self.s = s + "$"
        self.root = SuffixTreeNode()
        for i in range(len(self.s)):
            self._insert(i)

    def _insert(self, index):
        curr = self.root
        for i in range(index, len(self.s)):
            char = self.s[i]
            if char not in curr.children:
                curr.children[char] = SuffixTreeNode(i, len(self.s))
                return
            curr = curr.children[char]

if __name__ == "__main__":
    s = "banana"
    st = SuffixTree(s)
    print(f"Suffix tree for '{s}' created.")
