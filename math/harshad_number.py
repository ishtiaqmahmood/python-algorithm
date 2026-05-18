def is_harshad(n):
    """
    Checks if a number is a Harshad number (or Niven number).
    A Harshad number is an integer that is divisible by the sum of its digits.

    Args:
        n (int): Input number.

    Returns:
        bool: True if Harshad, False otherwise.
    """
    if n <= 0:
        return False
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0


if __name__ == "__main__":
    for i in [18, 19, 21]:
        print(f"Is {i} Harshad? {is_harshad(i)}")
