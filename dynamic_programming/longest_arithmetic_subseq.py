def longest_arith_seq_length(nums):
    """
    Longest Arithmetic Subsequence.
    """
    dp = {}
    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i, diff] = dp.get((j, diff), 1) + 1
    return max(dp.values()) if dp else 0


if __name__ == "__main__":
    print(f"Longest arithmetic subseq: {longest_arith_seq_length([3, 6, 9, 12])}")
