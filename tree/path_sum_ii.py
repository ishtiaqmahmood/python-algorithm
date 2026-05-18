class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum_ii(root, target_sum):
    """
    Finds all root-to-leaf paths where each path's sum equals target_sum.

    Args:
        root (TreeNode): Root of the tree.
        target_sum (int): Target sum.

    Returns:
        list: List of paths.
    """
    res = []
    def dfs(node, current_sum, path):
        if not node:
            return
        current_sum += node.val
        path.append(node.val)
        if not node.left and not node.right and current_sum == target_sum:
            res.append(list(path))
        else:
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
        path.pop()

    dfs(root, 0, [])
    return res


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    print(f"Path Sum II (target=22): {path_sum_ii(root, 22)}")
