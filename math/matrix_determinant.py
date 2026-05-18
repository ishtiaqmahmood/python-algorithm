def get_matrix_minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]


def matrix_determinant(m):
    """
    Calculates the determinant of a square matrix.
    """
    if len(m) == 1: return m[0][0]
    if len(m) == 2: return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    det = 0
    for c in range(len(m)):
        det += ((-1)**c) * m[0][c] * matrix_determinant(get_matrix_minor(m, 0, c))
    return det


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Determinant: {matrix_determinant(m)}") # Should be 0
    m2 = [[4, 3], [3, 2]]
    print(f"Determinant: {matrix_determinant(m2)}") # -1
