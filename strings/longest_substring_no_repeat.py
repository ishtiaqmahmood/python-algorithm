def length_of_longest_substring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s (str): Input string.

    Returns:
        int: Length of longest substring.
    """
    used = {}
    start = max_len = 0
    for i, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[char] = i
    return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    print(f"Length of longest substring without repeating chars in '{s}': {length_of_longest_substring(s)}")
