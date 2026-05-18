def line_intersection(line1, line2):
    """
    Finds the intersection point of two lines.
    Lines are represented as ((x1, y1), (x2, y2)).

    Args:
        line1 (tuple): First line.
        line2 (tuple): Second line.

    Returns:
        tuple: Intersection point (x, y), or None if parallel.
    """
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return None

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return (x, y)


if __name__ == "__main__":
    l1 = ((0, 0), (4, 4))
    l2 = ((0, 4), (4, 0))
    print(f"Intersection: {line_intersection(l1, l2)}")
