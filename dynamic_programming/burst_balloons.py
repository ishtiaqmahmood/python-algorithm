def max_coins(nums):
    """
    Burst Balloons.
    """
    nums = [1] + [x for x in nums if x > 0] + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n - 1):
        for left in range(n - length - 1):
            right = left + length + 1
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right],
                                     nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n-1]


if __name__ == "__main__":
    print(f"Max coins: {max_coins([3, 1, 5, 8])}")
