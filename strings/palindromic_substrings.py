def count_substrings(s):
    """
    Counts how many palindromic substrings in a string.

    Args:
        s (str): Input string.

    Returns:
        int: Count of palindromic substrings.
    """
    count = 0
    n = len(s)
    for i in range(2 * n - 1):
        l = i // 2
        r = l + i % 2
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count


if __name__ == "__main__":
    for s in ["abc", "aaa"]:
        print(f"Palindromic substrings in '{s}': {count_substrings(s)}")
