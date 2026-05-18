def matrix_trace(m):
    """
    Calculates the trace of a square matrix (sum of elements on the main diagonal).
    """
    return sum(m[i][i] for i in range(len(m)))


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Trace: {matrix_trace(m)}")
