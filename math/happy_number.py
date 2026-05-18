def is_happy(n):
    """
    Checks if a number is a happy number.
    A happy number is defined by the following process: Starting with any
    positive integer, replace the number by the sum of the squares of its
    digits, and repeat the process until the number equals 1, or it loops
    endlessly in a cycle which does not include 1.

    Args:
        n (int): Input number.

    Returns:
        bool: True if happy, False otherwise.
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1


if __name__ == "__main__":
    for i in [19, 2, 7]:
        print(f"Is {i} happy? {is_happy(i)}")
