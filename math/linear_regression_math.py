def linear_regression(x, y):
    """
    Simple Linear Regression (y = mx + b).
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi**2 for xi in x)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
    b = (sum_y - m * sum_x) / n
    return m, b


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    m, b = linear_regression(x, y)
    print(f"Line: y = {m}x + {b}")
