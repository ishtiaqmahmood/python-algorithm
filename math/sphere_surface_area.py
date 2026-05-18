import math


def sphere_surface_area(radius):
    """
    Calculates the surface area of a sphere.
    """
    return 4 * math.pi * radius**2


if __name__ == "__main__":
    print(f"Surface area of sphere (r=5): {sphere_surface_area(5)}")
