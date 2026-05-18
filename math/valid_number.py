def is_number(s):
    """
    Checks if a string is a valid number.

    Args:
        s (str): Input string.

    Returns:
        bool: True if valid number, False otherwise.
    """
    s = s.strip()
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    for s in ["0", " 0.1 ", "abc", "1 a", "2e10", " -90e3   "]:
        print(f"Is '{s}' a valid number? {is_number(s)}")
