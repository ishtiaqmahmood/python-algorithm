class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_pre_in(preorder, inorder):
    """
    Constructs binary tree from preorder and inorder traversal.

    Args:
        preorder (list): Preorder list.
        inorder (list): Inorder list.

    Returns:
        TreeNode: Root of tree.
    """
    if not inorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    idx = inorder.index(root_val)

    root.left = build_tree_pre_in(preorder, inorder[:idx])
    root.right = build_tree_pre_in(preorder, inorder[idx+1:])
    return root


if __name__ == "__main__":
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    root = build_tree_pre_in(pre, ino)
    print(f"Tree built with root: {root.val}")
