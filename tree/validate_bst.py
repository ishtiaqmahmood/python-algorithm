class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    """
    Validates if a tree is a Binary Search Tree.

    Args:
        root (TreeNode): Root of tree.

    Returns:
        bool: True if valid.
    """
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root)


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Is valid BST? {is_valid_bst(root)}")
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(f"Is valid BST? {is_valid_bst(root)}")
