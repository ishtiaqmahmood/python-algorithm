def is_planar(n, edges):
    """
    Checks if a graph is planar (conceptual).
    Uses Euler's formula (e <= 3v - 6) as a necessary condition for v >= 3.
    """
    if n < 3: return True
    return len(edges) <= 3 * n - 6


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 0)]
    print(f"Is planar (check e <= 3v-6)? {is_planar(3, edges)}")
