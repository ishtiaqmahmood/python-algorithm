def generate_pascals_triangle(n):
    """
    Generates the first n rows of Pascal's Triangle.

    Args:
        n (int): Number of rows.

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    n = 5
    triangle = generate_pascals_triangle(n)
    for row in triangle:
        print(row)
