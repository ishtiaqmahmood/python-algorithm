def single_number(nums):
    """
    Finds the single number in a list where every other element appears twice.

    Args:
        nums (list): List of integers.

    Returns:
        int: The single number.
    """
    res = 0
    for num in nums:
        res ^= num
    return res


if __name__ == "__main__":
    test_nums = [4, 1, 2, 1, 2]
    print(f"Single number in {test_nums}: {single_number(test_nums)}")
