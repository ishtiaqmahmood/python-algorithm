class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_post_in(inorder, postorder):
    """
    Constructs binary tree from inorder and postorder traversal.

    Args:
        inorder (list): Inorder list.
        postorder (list): Postorder list.

    Returns:
        TreeNode: Root of tree.
    """
    if not inorder:
        return None

    root_val = postorder.pop()
    root = TreeNode(root_val)
    idx = inorder.index(root_val)

    root.right = build_tree_post_in(inorder[idx+1:], postorder)
    root.left = build_tree_post_in(inorder[:idx], postorder)
    return root


if __name__ == "__main__":
    ino = [9, 3, 15, 20, 7]
    post = [9, 15, 7, 20, 3]
    root = build_tree_post_in(ino, post)
    print(f"Tree built with root: {root.val}")
