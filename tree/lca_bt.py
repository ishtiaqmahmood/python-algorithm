class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor_bt(root, p, q):
    """
    Finds the LCA of two nodes in a Binary Tree.

    Args:
        root (TreeNode): Root of tree.
        p (TreeNode): Node 1.
        q (TreeNode): Node 2.

    Returns:
        TreeNode: LCA node.
    """
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor_bt(root.left, p, q)
    right = lowest_common_ancestor_bt(root.right, p, q)

    if left and right:
        return root
    return left if left else right


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5); root.right = TreeNode(1)
    p = root.left; q = root.right
    lca = lowest_common_ancestor_bt(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {lca.val}")
