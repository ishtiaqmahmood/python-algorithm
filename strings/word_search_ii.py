def find_words(board, words):
    """
    Finds all words from the list that can be formed by characters in the board.

    Args:
        board (list): 2D list of characters.
        words (list): List of strings.

    Returns:
        list: List of found words.
    """
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = word

    res = set()
    rows, cols = len(board), len(board[0])

    def dfs(r, c, node):
        char = board[r][c]
        if char not in node:
            return

        node = node[char]
        if '#' in node:
            res.add(node['#'])

        board[r][c] = '*'
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '*':
                dfs(nr, nc, node)
        board[r][c] = char

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie)

    return list(res)


if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(f"Found words: {find_words(board, words)}")
