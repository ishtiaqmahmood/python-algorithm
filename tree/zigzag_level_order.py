from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    """
    Zigzag level order traversal of a binary tree.

    Args:
        root (TreeNode): Root of the tree.

    Returns:
        list: Zigzag level order traversal list.
    """
    if not root:
        return []
    res = []
    queue = deque([root])
    reverse = False
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if reverse:
                level.appendleft(node.val)
            else:
                level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(list(level))
        reverse = not reverse
    return res


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(f"Zigzag Level Order: {zigzag_level_order(root)}")
