def is_armstrong(n):
    """
    Checks if a number is an Armstrong number.

    Args:
        n (int): Input number.

    Returns:
        bool: True if Armstrong, False otherwise.
    """
    s = str(n)
    power = len(s)
    total = sum(int(digit) ** power for digit in s)
    return total == n


if __name__ == "__main__":
    print(f"Is 153 Armstrong? {is_armstrong(153)}")
    print(f"Is 123 Armstrong? {is_armstrong(123)}")
