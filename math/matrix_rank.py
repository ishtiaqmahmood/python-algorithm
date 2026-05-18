def matrix_rank(matrix):
    """
    Finds the rank of a matrix using Gaussian elimination.
    """
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    rank = n
    mat = [row[:] for row in matrix]

    for row in range(rank):
        if mat[row][row] != 0:
            for col in range(m):
                if col != row:
                    mult = mat[col][row] / mat[row][row]
                    for i in range(rank):
                        mat[col][i] -= mult * mat[row][i]
        else:
            reduce = True
            for i in range(row + 1, m):
                if mat[i][row] != 0:
                    mat[row], mat[i] = mat[i], mat[row]
                    reduce = False
                    break
            if reduce:
                rank -= 1
                for i in range(m):
                    mat[i][row] = mat[i][rank]
            row -= 1
    return rank


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Rank: {matrix_rank(m)}")
