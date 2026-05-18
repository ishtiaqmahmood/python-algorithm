class Node:
    def __init__(self, val=None):
        self.keys = []
        if val is not None: self.keys.append(val)
        self.children = []


class TwoThreeTree:
    """
    2-3 Tree implementation (conceptual).
    """
    def __init__(self):
        self.root = None


if __name__ == "__main__":
    tt = TwoThreeTree()
    print("2-3 Tree initialized.")
