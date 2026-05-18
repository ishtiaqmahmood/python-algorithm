def group_shifted_strings(strings):
    """
    Groups strings that belong to the same shifting sequence.

    Args:
        strings (list): List of strings.

    Returns:
        list: Grouped strings.
    """
    groups = {}
    for s in strings:
        key = []
        for i in range(len(s) - 1):
            diff = (ord(s[i+1]) - ord(s[i])) % 26
            key.append(diff)
        key = tuple(key)
        groups.setdefault(key, []).append(s)
    return list(groups.values())


if __name__ == "__main__":
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(f"Grouped shifted strings: {group_shifted_strings(strings)}")
