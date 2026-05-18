class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor_bst(root, p, q):
    """
    Finds the LCA of two nodes in a BST.

    Args:
        root (TreeNode): Root of BST.
        p (TreeNode): Node 1.
        q (TreeNode): Node 2.

    Returns:
        TreeNode: LCA node.
    """
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
    return None


if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2); root.right = TreeNode(8)
    p = root.left; q = root.right
    lca = lowest_common_ancestor_bst(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {lca.val}")
