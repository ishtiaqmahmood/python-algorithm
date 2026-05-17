def solve_knight_tour(n):
    """
    Solves the Knight's Tour problem on an n x n board.

    Args:
        n (int): Board size.

    Returns:
        list: n x n board with move numbers.
    """
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0

    def backtrack(curr_x, curr_y, pos):
        if pos == n * n:
            return True

        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]
            if 0 <= new_x < n and 0 <= new_y < n and board[new_x][new_y] == -1:
                board[new_x][new_y] = pos
                if backtrack(new_x, new_y, pos + 1):
                    return True
                board[new_x][new_y] = -1
        return False

    if backtrack(0, 0, 1):
        return board
    return None


if __name__ == "__main__":
    board_size = 5
    result_board = solve_knight_tour(board_size)
    if result_board:
        for row in result_board:
            print(row)
    else:
        print("No solution exists")
