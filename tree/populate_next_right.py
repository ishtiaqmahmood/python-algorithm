class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    """
    Populates each next pointer to point to its next right node.

    Args:
        root (Node): Root of tree.

    Returns:
        Node: Root with next pointers.
    """
    if not root:
        return None

    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root


if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    connect(root)
    print("Next pointers connected.")
