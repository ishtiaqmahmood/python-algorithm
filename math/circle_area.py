import math


def circle_area(radius):
    """
    Calculates the area of a circle.
    """
    return math.pi * radius**2


if __name__ == "__main__":
    print(f"Area of circle (r=5): {circle_area(5)}")
