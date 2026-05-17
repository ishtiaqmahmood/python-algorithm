def is_palindrome_num(n):
    """
    Checks if an integer is a palindrome.

    Args:
        n (int): Input integer.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    if n < 0:
        return False
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    print(f"Is 121 palindrome? {is_palindrome_num(121)}")
    print(f"Is -121 palindrome? {is_palindrome_num(-121)}")
