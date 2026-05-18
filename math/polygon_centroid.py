def polygon_centroid(points):
    """
    Calculates the centroid of a non-self-intersecting closed polygon.

    Args:
        points (list): List of (x, y) tuples.

    Returns:
        tuple: (cx, cy) centroid coordinates.
    """
    area = 0
    cx = 0
    cy = 0
    n = len(points)
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        factor = (p1[0] * p2[1] - p2[0] * p1[1])
        area += factor
        cx += (p1[0] + p2[0]) * factor
        cy += (p1[1] + p2[1]) * factor

    area /= 2.0
    cx /= (6 * area)
    cy /= (6 * area)
    return (cx, cy)


if __name__ == "__main__":
    pts = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(f"Centroid of rectangle: {polygon_centroid(pts)}")
