def permute_unique(nums):
    """
    Permutations II (With duplicates).
    """
    res = []
    nums.sort()

    def backtrack(curr, used):
        if len(curr) == len(nums):
            res.append(list(curr))
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            curr.append(nums[i])
            backtrack(curr, used)
            curr.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return res


if __name__ == "__main__":
    print(f"Permutations: {permute_unique([1, 1, 2])}")
