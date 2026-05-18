def calculate(s):
    """
    Evaluates a basic calculator expression (including +, -, (, )).

    Args:
        s (str): Expression.

    Returns:
        int: Result.
    """
    stack = []
    res = 0
    num = 0
    sign = 1
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in "+-":
            res += sign * num
            num = 0
            sign = 1 if char == "+" else -1
        elif char == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif char == ")":
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
    return res + sign * num


if __name__ == "__main__":
    for s in ["1 + 1", " 2-1 + 2 ", "(1+(4+5+2)-3)+(6+8)"]:
        print(f"calculate('{s}') = {calculate(s)}")
