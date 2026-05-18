def area_of_polygon(points):
    """
    Calculates the area of a non-self-intersecting polygon using the Shoelace formula.

    Args:
        points (list): List of (x, y) tuples representing the vertices.

    Returns:
        float: Area of the polygon.
    """
    n = len(points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0


if __name__ == "__main__":
    polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(f"Area of rectangle: {area_of_polygon(polygon)}")
