def is_anagram(s, t):
    """
    Checks if t is an anagram of s.

    Args:
        s (str): First string.
        t (str): Second string.

    Returns:
        bool: True if anagram, False otherwise.
    """
    if len(s) != len(t):
        return False

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
    return True


if __name__ == "__main__":
    for s, t in [("anagram", "nagaram"), ("rat", "car")]:
        print(f"Are '{s}' and '{t}' anagrams? {is_anagram(s, t)}")
