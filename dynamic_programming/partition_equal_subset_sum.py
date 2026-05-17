def can_partition(nums):
    """
    Determines if a list can be partitioned into two subsets with equal sums.

    Args:
        nums (list): List of numbers.

    Returns:
        bool: True if partition exists, False otherwise.
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    n = len(nums)
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]


if __name__ == "__main__":
    test_nums = [1, 5, 11, 5]
    print(f"Can partition {test_nums} into equal sums: {can_partition(test_nums)}")
