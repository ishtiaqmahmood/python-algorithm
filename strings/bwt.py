def bwt_encode(s):
    """
    Burrows-Wheeler Transform encoding.

    Args:
        s (str): Input string.

    Returns:
        str: BWT of s.
    """
    s += '$'
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    return "".join(row[-1] for row in table)


def bwt_decode(s):
    """
    Burrows-Wheeler Transform decoding.

    Args:
        s (str): BWT encoded string.

    Returns:
        str: Decoded original string.
    """
    table = [""] * len(s)
    for _ in range(len(s)):
        table = sorted(s[i] + table[i] for i in range(len(s)))
    s = [row for row in table if row.endswith('$')][0]
    return s[:-1]


if __name__ == "__main__":
    s = "banana"
    encoded = bwt_encode(s)
    print(f"BWT Encoded: {encoded}")
    print(f"BWT Decoded: {bwt_decode(encoded)}")
