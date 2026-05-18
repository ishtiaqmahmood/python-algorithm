def is_inside_polygon(points, p):
    """
    Checks if a point p is inside a polygon using the Ray Casting algorithm.

    Args:
        points (list): List of (x, y) tuples representing the vertices.
        p (tuple): The point to check (x, y).

    Returns:
        bool: True if inside, False otherwise.
    """
    n = len(points)
    inside = False
    x, y = p
    p1x, p1y = points[0]
    for i in range(n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


if __name__ == "__main__":
    polygon = [(0, 0), (10, 0), (10, 10), (0, 10)]
    print(f"Is (5, 5) inside? {is_inside_polygon(polygon, (5, 5))}")
    print(f"Is (15, 5) inside? {is_inside_polygon(polygon, (15, 5))}")
