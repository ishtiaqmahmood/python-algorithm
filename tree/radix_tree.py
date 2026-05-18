class RadixNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class RadixTree:
    """
    Radix Tree (Compressed Trie) implementation.
    """
    def __init__(self):
        self.root = RadixNode()

    def insert(self, word):
        curr = self.root
        i = 0
        while i < len(word):
            found = False
            for edge in curr.children:
                common = 0
                while common < len(edge) and i + common < len(word) and edge[common] == word[i + common]:
                    common += 1
                if common > 0:
                    found = True
                    if common == len(edge):
                        curr = curr.children[edge]
                        i += common
                    else:
                        # Split edge
                        child = curr.children.pop(edge)
                        split_node = RadixNode()
                        curr.children[edge[:common]] = split_node
                        split_node.children[edge[common:]] = child
                        curr = split_node
                        i += common
                    break
            if not found:
                curr.children[word[i:]] = RadixNode()
                curr.children[word[i:]].is_end = True
                return
        curr.is_end = True


if __name__ == "__main__":
    rt = RadixTree()
    rt.insert("romane")
    rt.insert("romanus")
    print("Radix Tree words inserted.")
