def multiply_strings(num1, num2):
    """
    Multiplies two non-negative integers represented as strings.

    Args:
        num1 (str): First number.
        num2 (str): Second number.

    Returns:
        str: Product as string.
    """
    if num1 == "0" or num2 == "0":
        return "0"

    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            sum_val = mul + res[p2]
            res[p2] = sum_val % 10
            res[p1] += sum_val // 10

    res_str = "".join(map(str, res))
    return res_str.lstrip("0")


if __name__ == "__main__":
    print(f"'123' * '456' = {multiply_strings('123', '456')}")
