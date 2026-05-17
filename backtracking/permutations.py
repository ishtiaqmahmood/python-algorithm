def get_permutations(nums):
    """
    Generates all permutations of a list of numbers.

    Args:
        nums (list): Input list.

    Returns:
        list: List of all permutations.
    """
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(f"Permutations of {test_nums}: {get_permutations(test_nums)}")
