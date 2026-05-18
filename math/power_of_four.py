def is_power_of_four(n):
    """
    Checks if a number is a power of four.

    Args:
        n (int): Input number.

    Returns:
        bool: True if power of four, False otherwise.
    """
    return n > 0 and (n & (n - 1)) == 0 and (n % 3 == 1)


if __name__ == "__main__":
    for i in [16, 8, 1, 64]:
        print(f"Is {i} power of 4? {is_power_of_four(i)}")
