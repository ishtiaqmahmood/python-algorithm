def check_odd_even(n):
    """
    Checks if an integer is odd or even using bit manipulation.

    Args:
        n (int): Input integer.

    Returns:
        str: "Even" or "Odd".
    """
    return "Even" if (n & 1) == 0 else "Odd"


if __name__ == "__main__":
    print(f"10 is {check_odd_even(10)}")
    print(f"11 is {check_odd_even(11)}")
