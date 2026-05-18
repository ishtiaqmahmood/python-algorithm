def is_valid(board, r, c, val):
    for i in range(9):
        if board[r][i] == val or board[i][c] == val: return False
        if board[3*(r//3) + i//3][3*(c//3) + i%3] == val: return False
    return True


def solve_sudoku(board):
    """
    Sudoku Solver using Backtracking.
    """
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                for val in "123456789":
                    if is_valid(board, r, c, val):
                        board[r][c] = val
                        if solve_sudoku(board): return True
                        board[r][c] = '.'
                return False
    return True


if __name__ == "__main__":
    # Example Sudoku board...
    print("Sudoku solver optimized initialized.")
