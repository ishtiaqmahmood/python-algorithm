def single_number_iii(nums):
    """
    Single Number III (Exactly two elements appear only once).
    """
    diff = 0
    for x in nums: diff ^= x
    diff &= -diff

    res = [0, 0]
    for x in nums:
        if x & diff: res[0] ^= x
        else: res[1] ^= x
    return res


if __name__ == "__main__":
    print(f"Single numbers: {single_number_iii([1, 2, 1, 3, 2, 5])}")
