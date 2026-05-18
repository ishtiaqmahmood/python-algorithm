import math


def sphere_volume(radius):
    return (4/3) * math.pi * (radius**3)


def cylinder_volume(radius, height):
    return math.pi * (radius**2) * height


def cone_volume(radius, height):
    return (1/3) * math.pi * (radius**2) * height


if __name__ == "__main__":
    r, h = 5, 10
    print(f"Sphere Volume (r={r}): {sphere_volume(r)}")
    print(f"Cylinder Volume (r={r}, h={h}): {cylinder_volume(r, h)}")
    print(f"Cone Volume (r={r}, h={h}): {cone_volume(r, h)}")
