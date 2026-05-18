def word_pattern(pattern, s):
    """
    Checks if s follows the same pattern.

    Args:
        pattern (str): Pattern string.
        s (str): Space-separated words string.

    Returns:
        bool: True if it follows pattern, False otherwise.
    """
    words = s.split()
    if len(pattern) != len(words):
        return False

    p_to_w = {}
    w_to_p = {}
    for p, w in zip(pattern, words):
        if p not in p_to_w:
            p_to_w[p] = w
        if w not in w_to_p:
            w_to_p[w] = p
        if p_to_w[p] != w or w_to_p[w] != p:
            return False
    return True


if __name__ == "__main__":
    pattern, s = "abba", "dog cat cat dog"
    print(f"Pattern '{pattern}' with '{s}': {word_pattern(pattern, s)}")
