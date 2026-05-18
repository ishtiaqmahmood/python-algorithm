def length_of_last_word(s):
    """
    Returns the length of the last word in a string.

    Args:
        s (str): Input string.

    Returns:
        int: Length of last word.
    """
    words = s.split()
    return len(words[-1]) if words else 0


if __name__ == "__main__":
    for s in ["Hello World", "   fly me   to   the moon  "]:
        print(f"Length of last word in '{s}': {length_of_last_word(s)}")
