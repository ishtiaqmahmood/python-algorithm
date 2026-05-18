def max_sum_of_three_subarrays(nums, k):
    """
    Maximum Sum of 3 Non-Overlapping Subarrays.
    """
    n = len(nums)
    sums = [0] * (n - k + 1)
    cur = sum(nums[:k])
    sums[0] = cur
    for i in range(1, n - k + 1):
        cur += nums[i+k-1] - nums[i-1]
        sums[i] = cur

    left = [0] * len(sums)
    best = 0
    for i in range(len(sums)):
        if sums[i] > sums[best]:
            best = i
        left[i] = best

    right = [0] * len(sums)
    best = len(sums) - 1
    for i in range(len(sums) - 1, -1, -1):
        if sums[i] >= sums[best]:
            best = i
        right[i] = best

    res = [-1, -1, -1]
    for i in range(k, len(sums) - k):
        l, r = left[i-k], right[i+k]
        if res[0] == -1 or sums[l] + sums[i] + sums[r] > sums[res[0]] + sums[res[1]] + sums[res[2]]:
            res = [l, i, r]
    return res


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    print(f"Indices of 3 subarrays: {max_sum_of_three_subarrays(nums, 2)}")
