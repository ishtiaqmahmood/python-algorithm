import sys

def matrix_chain_multiplication(p):
    """
    Finds the most efficient way to multiply a chain of matrices.

    Args:
        p (list): List of dimensions of matrices.

    Returns:
        int: Minimum number of multiplications.
    """
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
    return dp[0][n - 1]


if __name__ == "__main__":
    dims = [10, 20, 30, 40, 30]
    print(f"Min multiplications for {dims}: {matrix_chain_multiplication(dims)}")
