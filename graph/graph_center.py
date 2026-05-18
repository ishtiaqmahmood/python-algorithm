def graph_center(n, dist_matrix):
    """
    Finds the center of a graph (vertices with minimum eccentricity).
    """
    eccentricities = [max(row) for row in dist_matrix]
    min_ecc = min(eccentricities)
    return [i for i, ecc in enumerate(eccentricities) if ecc == min_ecc]


if __name__ == "__main__":
    dist = [[0, 1, 2], [1, 0, 1], [2, 1, 0]]
    print(f"Graph Center: {graph_center(3, dist)}")
