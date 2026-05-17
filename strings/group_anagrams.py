from collections import defaultdict

def group_anagrams(strs):
    """
    Groups anagrams together.

    Args:
        strs (list): List of strings.

    Returns:
        list: List of groups of anagrams.
    """
    anagrams = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        anagrams[tuple(count)].append(s)
    return list(anagrams.values())


if __name__ == "__main__":
    test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Grouped anagrams: {group_anagrams(test_strs)}")
