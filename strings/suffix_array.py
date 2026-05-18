def build_suffix_array(s):
    """
    Builds the suffix array for a given string s.
    Suffix array is a sorted list of all suffixes of s, represented by their starting indices.

    Args:
        s (str): Input string.

    Returns:
        list: Suffix array.
    """
    suffixes = sorted([(s[i:], i) for i in range(len(s))])
    return [suffix[1] for suffix in suffixes]


if __name__ == "__main__":
    s = "banana"
    print(f"Suffix array of '{s}': {build_suffix_array(s)}")
