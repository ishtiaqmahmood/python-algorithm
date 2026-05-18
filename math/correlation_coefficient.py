import math


def correlation_coefficient(x, y):
    """
    Calculates Pearson correlation coefficient.
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(xi**2 for xi in x)
    sum_y_sq = sum(yi**2 for yi in y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    num = (n * sum_xy - sum_x * sum_y)
    den = math.sqrt((n * sum_x_sq - sum_x**2) * (n * sum_y_sq - sum_y**2))
    return num / den if den != 0 else 0


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    print(f"Correlation: {correlation_coefficient(x, y)}")
