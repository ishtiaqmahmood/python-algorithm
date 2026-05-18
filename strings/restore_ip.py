def restore_ip_addresses(s):
    """
    Restores all possible valid IP addresses from a string of digits.

    Args:
        s (str): Input string.

    Returns:
        list: Valid IP addresses.
    """
    res = []

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append(".".join(path))
            return

        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start: start + length]
            if (segment.startswith('0') and len(segment) > 1) or (length == 3 and int(segment) > 255):
                continue
            backtrack(start + length, path + [segment])

    backtrack(0, [])
    return res


if __name__ == "__main__":
    for s in ["25525511135", "0000", "101023"]:
        print(f"IP addresses from '{s}': {restore_ip_addresses(s)}")
