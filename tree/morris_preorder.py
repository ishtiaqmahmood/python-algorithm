class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def morris_preorder(root):
    """
    Performs Morris Preorder Traversal (O(n) time, O(1) space).

    Args:
        root (TreeNode): Root of the tree.

    Returns:
        list: Preorder traversal list.
    """
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right

            if not prev.right:
                res.append(curr.val)
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return res


if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(f"Morris Preorder: {morris_preorder(root)}")
