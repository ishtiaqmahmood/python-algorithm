def is_scramble(s1, s2):
    """
    Checks if s2 is a scrambled string of s1.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if s2 is scramble of s1, False otherwise.
    """
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    n = len(s1)
    for i in range(1, n):
        if (is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])) or \
           (is_scramble(s1[:i], s2[n-i:]) and is_scramble(s1[i:], s2[:n-i])):
            return True
    return False


if __name__ == "__main__":
    s1, s2 = "great", "rgeat"
    print(f"Is '{s2}' scramble of '{s1}'? {is_scramble(s1, s2)}")
