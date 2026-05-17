from collections import Counter

def is_anagram(s1, s2):
    """
    Checks if two strings are anagrams of each other.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if anagrams, False otherwise.
    """
    return Counter(s1) == Counter(s2)


if __name__ == "__main__":
    str1, str2 = "anagram", "nagaram"
    print(f"Are '{str1}' and '{str2}' anagrams? {is_anagram(str1, str2)}")
