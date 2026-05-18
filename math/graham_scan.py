def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0
    return 1 if val > 0 else 2


def graham_scan(points):
    """
    Graham Scan algorithm for Convex Hull.

    Args:
        points (list): List of (x, y) tuples.

    Returns:
        list: Convex hull points.
    """
    n = len(points)
    if n < 3: return points

    # Find the bottom-most point
    p0 = min(points, key=lambda p: (p[1], p[0]))

    # Sort points by polar angle with p0
    import math
    def get_angle(p):
        return math.atan2(p[1] - p0[1], p[0] - p0[0])

    sorted_pts = sorted(points, key=get_angle)

    hull = [sorted_pts[0], sorted_pts[1], sorted_pts[2]]
    for i in range(3, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_pts[i]) != 2:
            hull.pop()
        hull.append(sorted_pts[i])
    return hull


if __name__ == "__main__":
    pts = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    print(f"Convex Hull (Graham Scan): {graham_scan(pts)}")
