class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    """
    Checks if a tree is a mirror of itself.

    Args:
        root (TreeNode): Root of tree.

    Returns:
        bool: True if symmetric.
    """
    def is_mirror(t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return (t1.val == t2.val) and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)

    return is_mirror(root, root)


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    print(f"Is symmetric? {is_symmetric(root)}")
