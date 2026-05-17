def lis(arr):
    """
    Finds the length of the Longest Increasing Subsequence of a list.

    Args:
        arr (list): The list of numbers.

    Returns:
        int: Length of the LIS.
    """
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == "__main__":
    nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(f"LIS length of {nums}: {lis(nums)}")
