class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    """
    Finds the kth smallest element in a BST.

    Args:
        root (TreeNode): Root of BST.
        k (int): Index.

    Returns:
        int: kth smallest value.
    """
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(f"2nd smallest: {kth_smallest(root, 2)}")
