def minimum_total(triangle):
    """
    Triangle (Minimum path sum).
    """
    dp = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    return dp[0]


if __name__ == "__main__":
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(f"Min path sum in triangle: {minimum_total(tri)}")
