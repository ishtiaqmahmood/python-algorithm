import math


def judge_square_sum(c):
    """
    Checks if there exist non-negative integers a and b such that a^2 + b^2 = c.

    Args:
        c (int): Input integer.

    Returns:
        bool: True if such a and b exist, False otherwise.
    """
    a = 0
    while a * a <= c:
        b = math.sqrt(c - a * a)
        if b == int(b):
            return True
        a += 1
    return False


if __name__ == "__main__":
    for i in [5, 3, 2, 4]:
        print(f"Can {i} be sum of squares? {judge_square_sum(i)}")
