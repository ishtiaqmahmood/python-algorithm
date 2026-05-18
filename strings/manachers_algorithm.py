def manacher(s):
    """
    Manacher's algorithm to find the longest palindromic substring in O(n).

    Args:
        s (str): Input string.

    Returns:
        str: Longest palindromic substring.
    """
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0
    max_len = 0
    center_index = 0
    for i in range(n):
        mirror = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mirror])
        while i + 1 + p[i] < n and i - 1 - p[i] >= 0 and t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    start = (center_index - max_len) // 2
    return s[start: start + max_len]


if __name__ == "__main__":
    s = "babad"
    print(f"Longest palindromic substring of '{s}': {manacher(s)}")
