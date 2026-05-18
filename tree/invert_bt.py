class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    """
    Inverts a binary tree.

    Args:
        root (TreeNode): Root of tree.

    Returns:
        TreeNode: Inverted tree root.
    """
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(root)
    print(f"Inverted root's left: {inverted.left.val}, right: {inverted.right.val}")
