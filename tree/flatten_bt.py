class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    """
    Flattens a binary tree to a "linked list" in-place (preorder).

    Args:
        root (TreeNode): Root of tree.
    """
    if not root:
        return

    flatten(root.left)
    flatten(root.right)

    tmp_right = root.right
    root.right = root.left
    root.left = None

    curr = root
    while curr.right:
        curr = curr.right
    curr.right = tmp_right


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    flatten(root)
    print("Tree flattened.")
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")
