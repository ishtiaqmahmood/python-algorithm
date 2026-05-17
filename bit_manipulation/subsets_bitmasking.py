def subsets_bitmasking(nums):
    """
    Generates all subsets using bitmasking.

    Args:
        nums (list): Input numbers.

    Returns:
        list: List of all subsets.
    """
    n = len(nums)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        subsets.append(subset)
    return subsets


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(f"Subsets of {test_nums} (bitmasking): {subsets_bitmasking(test_nums)}")
