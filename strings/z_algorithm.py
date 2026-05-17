def z_algorithm(text, pattern):
    """
    Z-algorithm for pattern matching.

    Args:
        text (str): Input text.
        pattern (str): Pattern to search.

    Returns:
        list: Indices of matches.
    """
    s = pattern + "$" + text
    n = len(s)
    z = [0] * n
    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1

    result = []
    m = len(pattern)
    for i in range(n):
        if z[i] == m:
            result.append(i - m - 1)
    return result


if __name__ == "__main__":
    t = "baabaa"
    p = "aab"
    print(f"Z-algorithm matches at: {z_algorithm(t, p)}")
