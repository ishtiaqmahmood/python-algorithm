def restore_ip_addresses(s):
    """
    Restore IP Addresses (Backtracking).
    """
    res = []

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s): res.append(".".join(path))
            return
        for length in range(1, 4):
            if start + length > len(s): break
            seg = s[start:start+length]
            if (seg.startswith('0') and len(seg) > 1) or (int(seg) > 255): continue
            backtrack(start + length, path + [seg])

    backtrack(0, [])
    return res


if __name__ == "__main__":
    print(f"IPs from '25525511135': {restore_ip_addresses('25525511135')}")
