def on_segment(p, q, r):
    return q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and \
           q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0
    return 1 if val > 0 else 2


def do_intersect(p1, q1, p2, q2):
    """
    Checks if two line segments (p1, q1) and (p2, q2) intersect.
    """
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4: return True
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True
    return False


if __name__ == "__main__":
    p1, q1 = (1, 1), (10, 1)
    p2, q2 = (1, 2), (10, 2)
    print(f"Do segments intersect? {do_intersect(p1, q1, p2, q2)}")
    p3, q3 = (10, 0), (0, 10)
    p4, q4 = (0, 0), (10, 10)
    print(f"Do segments intersect? {do_intersect(p3, q3, p4, q4)}")
