def is_self_dividing(n):
    """
    Checks if a number is self-dividing.
    A self-dividing number is a number that is divisible by every digit it contains.

    Args:
        n (int): Input number.

    Returns:
        bool: True if self-dividing, False otherwise.
    """
    for d in str(n):
        if d == '0' or n % int(d) != 0:
            return False
    return True


def self_dividing_numbers(left, right):
    """
    Returns all self-dividing numbers in range [left, right].

    Args:
        left (int): Left bound.
        right (int): Right bound.

    Returns:
        list: List of self-dividing numbers.
    """
    return [i for i in range(left, right + 1) if is_self_dividing(i)]


if __name__ == "__main__":
    print(f"Self-dividing numbers in [1, 22]: {self_dividing_numbers(1, 22)}")
