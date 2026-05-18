class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def build_cartesian_tree(arr):
    """
    Builds a Cartesian tree from an array (Min-Heap property).

    Args:
        arr (list): Input array.

    Returns:
        Node: Root of Cartesian tree.
    """
    if not arr:
        return None

    stack = []
    for x in arr:
        last = None
        while stack and stack[-1].val > x:
            last = stack.pop()

        node = Node(x)
        if stack:
            stack[-1].right = node
        if last:
            node.left = last
        stack.append(node)

    return stack[0]


if __name__ == "__main__":
    arr = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]
    root = build_cartesian_tree(arr)
    print(f"Cartesian Tree root: {root.val}")
