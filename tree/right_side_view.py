class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    """
    Returns the values of the nodes you can see from the right side of the tree.

    Args:
        root (TreeNode): Root of the tree.

    Returns:
        list: Right side view list.
    """
    res = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(res):
            res.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return res


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(f"Right Side View: {right_side_view(root)}")
