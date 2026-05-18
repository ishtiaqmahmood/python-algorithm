def is_power_of_three(n):
    """
    Checks if a number is a power of three.

    Args:
        n (int): Input number.

    Returns:
        bool: True if power of three, False otherwise.
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


if __name__ == "__main__":
    for i in [27, 45, 1]:
        print(f"Is {i} power of 3? {is_power_of_three(i)}")
