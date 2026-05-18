class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right


def build_kd_tree(points, depth=0):
    """
    Builds a k-d tree from a list of points.

    Args:
        points (list): List of points (tuples).
        depth (int): Current depth.

    Returns:
        KDNode: Root of the tree.
    """
    n = len(points)
    if n == 0:
        return None

    k = len(points[0])
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = n // 2

    return KDNode(
        points[median],
        build_kd_tree(points[:median], depth + 1),
        build_kd_tree(points[median + 1:], depth + 1)
    )


if __name__ == "__main__":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    root = build_kd_tree(points)
    print(f"K-D Tree built with root: {root.point}")
