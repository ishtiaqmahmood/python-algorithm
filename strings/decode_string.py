def decode_string(s):
    """
    Decodes an encoded string like "3[a]2[bc]".

    Args:
        s (str): Encoded string.

    Returns:
        str: Decoded string.
    """
    stack = []
    cur_str = ""
    cur_num = 0
    for char in s:
        if char == '[':
            stack.append(cur_str)
            stack.append(cur_num)
            cur_str = ""
            cur_num = 0
        elif char == ']':
            num = stack.pop()
            prev_str = stack.pop()
            cur_str = prev_str + num * cur_str
        elif char.isdigit():
            cur_num = cur_num * 10 + int(char)
        else:
            cur_str += char
    return cur_str


if __name__ == "__main__":
    for s in ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]:
        print(f"decode_string('{s}') = '{decode_string(s)}'")
