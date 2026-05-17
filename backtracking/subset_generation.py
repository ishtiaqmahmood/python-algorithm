def get_subsets(nums):
    """
    Generates all possible subsets (power set).

    Args:
        nums (list): Input numbers.

    Returns:
        list: List of all subsets.
    """
    result = []

    def backtrack(index, current):
        result.append(current[:])
        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(f"Subsets of {test_nums}: {get_subsets(test_nums)}")
