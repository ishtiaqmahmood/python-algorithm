import math


def triangle_area(a, b, c):
    """
    Calculates the area of a triangle using Heron's formula.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    print(f"Area of triangle (3, 4, 5): {triangle_area(3, 4, 5)}")
