def all_pairs_shortest_paths_matrix(n, adj_matrix):
    """
    All-Pairs Shortest Paths using matrix multiplication-like approach (O(n^3 log n)).
    """
    dist = [row[:] for row in adj_matrix]

    def multiply(A, B):
        C = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] = min(C[i][j], A[i][k] + B[k][j])
        return C

    # Using repeated squaring
    m = 1
    while m < n - 1:
        dist = multiply(dist, dist)
        m *= 2
    return dist


if __name__ == "__main__":
    inf = float('inf')
    graph = [[0, 3, inf, 7], [8, 0, 2, inf], [5, inf, 0, 1], [2, inf, inf, 0]]
    print(f"APSP Matrix: {all_pairs_shortest_paths_matrix(4, graph)}")
