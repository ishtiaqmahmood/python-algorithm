def gaussian_elimination(A, b):
    """
    Solves Ax = b using Gaussian elimination.
    """
    n = len(A)
    for i in range(n):
        max_el = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j: A[k][j] = 0
                else: A[k][j] += c * A[i][j]
            b[k] += c * b[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]
    return x


if __name__ == "__main__":
    A = [[3, 2, -4], [2, 3, 3], [5, -3, 1]]
    b = [3, 15, 14]
    print(f"Solution: {gaussian_elimination(A, b)}")
