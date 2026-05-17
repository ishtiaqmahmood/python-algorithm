def longest_common_prefix(strs):
    """
    Finds the longest common prefix string amongst an array of strings.

    Args:
        strs (list): List of strings.

    Returns:
        str: Longest common prefix.
    """
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    test_strs = ["flower", "flow", "flight"]
    print(f"Longest common prefix of {test_strs}: {longest_common_prefix(test_strs)}")
