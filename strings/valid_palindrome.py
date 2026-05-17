def is_palindrome(s):
    """
    Checks if a string is a palindrome, ignoring non-alphanumeric characters and case.

    Args:
        s (str): Input string.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    print(f"Is '{test_str}' a palindrome? {is_palindrome(test_str)}")
