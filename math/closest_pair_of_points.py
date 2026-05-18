import math


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_pair(points):
    """
    Finds the closest pair of points in O(n log n).

    Args:
        points (list): List of (x, y) tuples.

    Returns:
        float: Minimum distance.
    """
    def solve(pts_x, pts_y):
        n = len(pts_x)
        if n <= 3:
            res = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    res = min(res, dist(pts_x[i], pts_x[j]))
            return res

        mid = n // 2
        mid_p = pts_x[mid]

        dl = solve(pts_x[:mid], [p for p in pts_y if p[0] <= mid_p[0]])
        dr = solve(pts_x[mid:], [p for p in pts_y if p[0] > mid_p[0]])
        d = min(dl, dr)

        strip = [p for p in pts_y if abs(p[0] - mid_p[0]) < d]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = min(d, dist(strip[i], strip[j]))
        return d

    points_x = sorted(points)
    points_y = sorted(points, key=lambda p: p[1])
    return solve(points_x, points_y)


if __name__ == "__main__":
    pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"Closest distance: {closest_pair(pts)}")
