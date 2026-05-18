def is_automorphic(n):
    """
    Checks if a number is an automorphic number.
    An automorphic number is a number whose square ends in the same digits as the number itself.

    Args:
        n (int): Input number.

    Returns:
        bool: True if automorphic, False otherwise.
    """
    sq = n * n
    return str(sq).endswith(str(n))


if __name__ == "__main__":
    for i in [5, 25, 76, 10]:
        print(f"Is {i} automorphic? {is_automorphic(i)}")
