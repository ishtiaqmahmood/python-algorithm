def longest_valid_parentheses(s):
    """
    Finds the length of the longest valid (well-formed) parentheses substring.

    Args:
        s (str): Input string.

    Returns:
        int: Length of longest valid substring.
    """
    stack = [-1]
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len


if __name__ == "__main__":
    for s in ["(()", ")()())", ""]:
        print(f"Longest valid in '{s}': {longest_valid_parentheses(s)}")
