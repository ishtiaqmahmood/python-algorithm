def predict_the_winner(nums):
    """
    Predict the Winner (optimal strategy).
    """
    n = len(nums)
    dp = nums[:]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i] = max(nums[i] - dp[i+1], nums[j] - dp[i])
    return dp[0] >= 0


if __name__ == "__main__":
    print(f"Can player 1 win? {predict_the_winner([1, 5, 2])}")
