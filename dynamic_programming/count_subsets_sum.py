def count_subsets(arr, k):
    """
    Counts the number of subsets with sum equal to k.
    """
    dp = [0] * (k + 1)
    dp[0] = 1
    for x in arr:
        for i in range(k, x - 1, -1):
            dp[i] += dp[i-x]
    return dp[k]


if __name__ == "__main__":
    print(f"Subset count (sum=6): {count_subsets([1, 2, 3, 3], 6)}")
