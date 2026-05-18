def add_binary(a, b):
    """
    Adds two binary strings and returns the result as a binary string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Sum as binary string.
    """
    res = ""
    i, j, carry = len(a) - 1, len(b) - 1, 0
    while i >= 0 or j >= 0 or carry:
        s = carry
        if i >= 0:
            s += int(a[i])
            i -= 1
        if j >= 0:
            s += int(b[j])
            j -= 1
        res = str(s % 2) + res
        carry = s // 2
    return res


if __name__ == "__main__":
    print(f"'11' + '1' = {add_binary('11', '1')}")
    print(f"'1010' + '1011' = {add_binary('1010', '1011')}")
