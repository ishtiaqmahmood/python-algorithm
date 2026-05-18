def total_hamming_distance(nums):
    """
    Total Hamming Distance.
    """
    res = 0
    for i in range(32):
        count = 0
        for x in nums:
            count += (x >> i) & 1
        res += count * (len(nums) - count)
    return res


if __name__ == "__main__":
    print(f"Total Hamming distance: {total_hamming_distance([4, 14, 2])}")
