def single_number_ii(nums):
    """
    Single Number II (Every element appears three times except for one).
    """
    ones = zeros = 0
    for x in nums:
        ones = (ones ^ x) & ~zeros
        zeros = (zeros ^ x) & ~ones
    return ones


if __name__ == "__main__":
    print(f"Single number: {single_number_ii([2, 2, 3, 2])}")
