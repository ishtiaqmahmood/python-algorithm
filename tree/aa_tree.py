class AANode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.level = 1


def skew(node):
    if not node or not node.left:
        return node
    if node.left.level == node.level:
        l = node.left
        node.left = l.right
        l.right = node
        return l
    return node


def split(node):
    if not node or not node.right or not node.right.right:
        return node
    if node.right.right.level == node.level:
        r = node.right
        node.right = r.left
        r.left = node
        r.level += 1
        return r
    return node


def insert(node, val):
    if not node:
        return AANode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    node = skew(node)
    node = split(node)
    return node


if __name__ == "__main__":
    root = None
    for x in [10, 20, 5, 15]:
        root = insert(root, x)
    print(f"AA Tree root: {root.val}")
