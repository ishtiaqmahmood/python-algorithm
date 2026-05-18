class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def update(node, l, r, idx, val):
    """
    Persistent Segment Tree update.
    """
    new_node = Node(node.val + val, node.left, node.right)
    if l == r:
        return new_node

    mid = (l + r) // 2
    if idx <= mid:
        if not node.left: node.left = Node()
        new_node.left = update(node.left, l, mid, idx, val)
    else:
        if not node.right: node.right = Node()
        new_node.right = update(node.right, mid + 1, r, idx, val)
    return new_node


if __name__ == "__main__":
    root = Node()
    v1 = update(root, 0, 10, 5, 1)
    v2 = update(v1, 0, 10, 2, 1)
    print("Persistent Segment Tree versions created.")
