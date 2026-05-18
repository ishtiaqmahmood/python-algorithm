def is_valid_parentheses(s):
    """
    Checks if a string of parentheses is valid.

    Args:
        s (str): Input string.

    Returns:
        bool: True if valid, False otherwise.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == "__main__":
    for s in ["()[]{}", "(]", "([)]", "{[]}"]:
        print(f"Is '{s}' valid? {is_valid_parentheses(s)}")
