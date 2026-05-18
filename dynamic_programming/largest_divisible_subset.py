def largest_divisible_subset(nums):
    """
    Largest Divisible Subset.
    """
    if not nums: return []
    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_idx = 0
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] > dp[max_idx]:
            max_idx = i

    res = []
    while max_idx != -1:
        res.append(nums[max_idx])
        max_idx = prev[max_idx]
    return res[::-1]


if __name__ == "__main__":
    print(f"Largest divisible subset: {largest_divisible_subset([1, 2, 4, 8])}")
