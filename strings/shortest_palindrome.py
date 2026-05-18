def shortest_palindrome(s):
    """
    Finds the shortest palindrome by adding characters in front of s.

    Args:
        s (str): Input string.

    Returns:
        str: Shortest palindrome.
    """
    if not s:
        return ""
    rev_s = s[::-1]
    l = s + "#" + rev_s
    p = [0] * len(l)
    for i in range(1, len(l)):
        j = p[i - 1]
        while j > 0 and l[i] != l[j]:
            j = p[j - 1]
        if l[i] == l[j]:
            j += 1
        p[i] = j
    return rev_s[:len(s) - p[-1]] + s


if __name__ == "__main__":
    for s in ["aacecaaa", "abcd"]:
        print(f"Shortest palindrome for '{s}': {shortest_palindrome(s)}")
