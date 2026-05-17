def is_valid(board, r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    start_r, start_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == num:
                return False
    return True

def solve_sudoku(board):
    """
    Solves a 9x9 Sudoku board using backtracking.

    Args:
        board (list): 2D list representing the Sudoku board.

    Returns:
        bool: True if solved, False otherwise.
    """
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if solve_sudoku(board):
                            return True
                        board[r][c] = 0
                return False
    return True


if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    if solve_sudoku(sudoku_board):
        for row in sudoku_board:
            print(row)
    else:
        print("No solution exists")
