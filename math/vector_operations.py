import math


def vector_add(v1, v2):
    return [x + y for x, y in zip(v1, v2)]


def vector_sub(v1, v2):
    return [x - y for x, y in zip(v1, v2)]


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def cross_product_3d(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]


if __name__ == "__main__":
    v1, v2 = [1, 2, 3], [4, 5, 6]
    print(f"Add: {vector_add(v1, v2)}")
    print(f"Dot: {dot_product(v1, v2)}")
    print(f"Cross: {cross_product_3d(v1, v2)}")
