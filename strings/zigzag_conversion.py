def zigzag_convert(s, num_rows):
    """
    Converts a string to zigzag pattern and reads it line by line.

    Args:
        s (str): Input string.
        num_rows (int): Number of rows.

    Returns:
        str: Converted string.
    """
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows = [''] * num_rows
    index, step = 0, 1
    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == num_rows - 1:
            step = -1
        index += step

    return "".join(rows)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    print(f"Zigzag conversion (3 rows): {zigzag_convert(s, 3)}")
