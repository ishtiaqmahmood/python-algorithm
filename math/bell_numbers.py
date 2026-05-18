def bell_number(n):
    """
    Computes the nth Bell number, which is the number of ways a set of
    n elements can be partitioned into non-empty subsets.

    Args:
        n (int): Number of elements.

    Returns:
        int: nth Bell number.
    """
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    return bell[n][0]


if __name__ == "__main__":
    for i in range(6):
        print(f"B_{i} = {bell_number(i)}")
