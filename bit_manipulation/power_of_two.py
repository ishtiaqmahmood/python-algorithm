def is_power_of_two(n):
    """
    Checks if an integer is a power of two.

    Args:
        n (int): Input integer.

    Returns:
        bool: True if power of two, False otherwise.
    """
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    print(f"Is 16 power of two? {is_power_of_two(16)}")
    print(f"Is 14 power of two? {is_power_of_two(14)}")
