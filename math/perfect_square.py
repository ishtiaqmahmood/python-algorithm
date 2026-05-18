def is_perfect_square(n):
    """
    Checks if a number is a perfect square using binary search.

    Args:
        n (int): Input number.

    Returns:
        bool: True if perfect square, False otherwise.
    """
    if n < 0:
        return False
    if n <= 1:
        return True

    left, right = 1, n // 2
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == n:
            return True
        elif sq < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    for i in [16, 14, 25, 1]:
        print(f"Is {i} perfect square? {is_perfect_square(i)}")
