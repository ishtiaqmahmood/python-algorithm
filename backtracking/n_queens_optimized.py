def solve_n_queens(n):
    """
    N-Queens Optimized with bitmasking or simple backtracking.
    """
    res = []
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)
    board = [['.'] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if not cols[c] and not diag1[r + c] and not diag2[r - c + n]:
                board[r][c] = 'Q'
                cols[c] = diag1[r + c] = diag2[r - c + n] = True
                backtrack(r + 1)
                board[r][c] = '.'
                cols[c] = diag1[r + c] = diag2[r - c + n] = False

    backtrack(0)
    return res


if __name__ == "__main__":
    print(f"Solutions for 4-Queens: {len(solve_n_queens(4))}")
