import math


def cholesky_decomposition(A):
    """
    Cholesky Decomposition of a symmetric positive-definite matrix.
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(A[i][i] - s)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - s))
    return L


if __name__ == "__main__":
    A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
    L = cholesky_decomposition(A)
    print(f"L: {L}")
