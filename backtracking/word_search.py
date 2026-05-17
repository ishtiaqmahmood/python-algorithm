def word_search(board, word):
    """
    Checks if a word exists in an m x n board of characters.

    Args:
        board (list): 2D list of characters.
        word (str): Target word.

    Returns:
        bool: True if word exists, False otherwise.
    """
    m, n = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = '#' # Mark as visited

        res = backtrack(r + 1, c, index + 1) or \
              backtrack(r - 1, c, index + 1) or \
              backtrack(r, c + 1, index + 1) or \
              backtrack(r, c - 1, index + 1)

        board[r][c] = temp # Restore
        return res

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True
    return False


if __name__ == "__main__":
    test_board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    test_word = "ABCCED"
    print(f"Word '{test_word}' exists in board: {word_search(test_board, test_word)}")
