import math


def qr_decomposition(A):
    """
    QR Decomposition using Gram-Schmidt process.
    """
    m = len(A)
    n = len(A[0])
    Q = [[0.0] * n for _ in range(m)]
    R = [[0.0] * n for _ in range(n)]

    for j in range(n):
        v = [A[i][j] for i in range(m)]
        for i in range(j):
            R[i][j] = sum(Q[k][i] * A[k][j] for k in range(m))
            for k in range(m):
                v[k] -= R[i][j] * Q[k][i]
        R[j][j] = math.sqrt(sum(x**2 for x in v))
        for k in range(m):
            Q[k][j] = v[k] / R[j][j]

    return Q, R


if __name__ == "__main__":
    A = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]]
    Q, R = qr_decomposition(A)
    print("QR Decomposition computed.")
