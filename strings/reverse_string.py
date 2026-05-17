def reverse_string(s):
    """
    Reverses a string.

    Args:
        s (str): Input string.

    Returns:
        str: Reversed string.
    """
    return s[::-1]


if __name__ == "__main__":
    test_str = "hello"
    print(f"Reverse of '{test_str}': {reverse_string(test_str)}")
