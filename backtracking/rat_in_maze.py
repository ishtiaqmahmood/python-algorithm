def solve_maze(maze):
    """
    Finds a path for the rat from (0,0) to (n-1, n-1) in a maze.

    Args:
        maze (list): 2D list where 1 is path and 0 is wall.

    Returns:
        list: Path as a sequence of (r, c) tuples.
    """
    n = len(maze)
    path = []

    def backtrack(r, c):
        if r == n - 1 and c == n - 1:
            path.append((r, c))
            return True

        if 0 <= r < n and 0 <= c < n and maze[r][c] == 1:
            maze[r][c] = 0 # Mark as visited
            path.append((r, c))

            if backtrack(r + 1, c) or backtrack(r, c + 1) or \
               backtrack(r - 1, c) or backtrack(r, c - 1):
                return True

            path.pop()
            # maze[r][c] = 1 # Backtrack visited mark if needed,
                             # but here it's to avoid cycles
        return False

    if backtrack(0, 0):
        return path
    return None


if __name__ == "__main__":
    test_maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    print(f"Rat path in maze: {solve_maze(test_maze)}")
