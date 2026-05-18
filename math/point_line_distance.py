import math


def point_to_line_distance(p, a, b):
    """
    Calculates the shortest distance from point p to line segment (a, b).

    Args:
        p, a, b (tuple): (x, y) coordinates.

    Returns:
        float: Distance.
    """
    px, py = p
    ax, ay = a
    bx, by = b

    l2 = (ax - bx)**2 + (ay - by)**2
    if l2 == 0: return math.sqrt((px - ax)**2 + (py - ay)**2)

    t = max(0, min(1, ((px - ax) * (bx - ax) + (py - ay) * (by - ay)) / l2))
    proj_x = ax + t * (bx - ax)
    proj_y = ay + t * (by - ay)

    return math.sqrt((px - proj_x)**2 + (py - proj_y)**2)


if __name__ == "__main__":
    print(f"Distance: {point_to_line_distance((0, 0), (1, 1), (1, -1))}")
