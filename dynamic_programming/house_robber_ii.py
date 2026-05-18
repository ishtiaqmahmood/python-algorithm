def rob_linear(nums):
    prev2, prev1 = 0, 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1


def rob(nums):
    """
    House Robber II (Circular houses).
    """
    if len(nums) == 1: return nums[0]
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))


if __name__ == "__main__":
    print(f"Max rob (circular): {rob([2, 3, 2])}")
