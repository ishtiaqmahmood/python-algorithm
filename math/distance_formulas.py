import math


def euclidean_distance(p1, p2):
    """
    Calculates the Euclidean distance between two points in n-dimensional space.

    Args:
        p1 (tuple): Point 1.
        p2 (tuple): Point 2.

    Returns:
        float: Euclidean distance.
    """
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))


def manhattan_distance(p1, p2):
    """
    Calculates the Manhattan distance between two points.

    Args:
        p1 (tuple): Point 1.
        p2 (tuple): Point 2.

    Returns:
        float: Manhattan distance.
    """
    return sum(abs(a - b) for a, b in zip(p1, p2))


if __name__ == "__main__":
    p1, p2 = (0, 0), (3, 4)
    print(f"Euclidean distance: {euclidean_distance(p1, p2)}")
    print(f"Manhattan distance: {manhattan_distance(p1, p2)}")
