def is_isomorphic(s, t):
    """
    Checks if two strings are isomorphic.

    Args:
        s (str): First string.
        t (str): Second string.

    Returns:
        bool: True if isomorphic, False otherwise.
    """
    if len(s) != len(t):
        return False

    mapping_s = {}
    mapping_t = {}
    for char_s, char_t in zip(s, t):
        if char_s not in mapping_s:
            mapping_s[char_s] = char_t
        if char_t not in mapping_t:
            mapping_t[char_t] = char_s
        if mapping_s[char_s] != char_t or mapping_t[char_t] != char_s:
            return False
    return True


if __name__ == "__main__":
    for s, t in [("egg", "add"), ("foo", "bar"), ("paper", "title")]:
        print(f"Are '{s}' and '{t}' isomorphic? {is_isomorphic(s, t)}")
