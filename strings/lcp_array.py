def build_suffix_array(s):
    suffixes = sorted([(s[i:], i) for i in range(len(s))])
    return [suffix[1] for suffix in suffixes]


def build_lcp_array(s, sa):
    """
    Builds the LCP (Longest Common Prefix) array using Kasai's algorithm.

    Args:
        s (str): Input string.
        sa (list): Suffix array of s.

    Returns:
        list: LCP array.
    """
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return lcp


if __name__ == "__main__":
    s = "banana"
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s, sa)
    print(f"Suffix Array: {sa}")
    print(f"LCP Array: {lcp}")
