def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all distinct solutions.

    Args:
        n (int): Number of queens.

    Returns:
        list: List of solutions (each solution is a list of strings).
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    pos_diag = set() # (r + c)
    neg_diag = set() # (r - c)

    def backtrack(r):
        if r == n:
            copy = [" ".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = '.'

    backtrack(0)
    return result


if __name__ == "__main__":
    n_q = 4
    solutions = solve_n_queens(n_q)
    print(f"Number of solutions for {n_q}-Queens: {len(solutions)}")
    for sol in solutions:
        for row in sol:
            print(row)
        print()
