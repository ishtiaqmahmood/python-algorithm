def hamming_distance(x, y):
    """
    Calculates the Hamming distance between two integers.

    Args:
        x (int): First integer.
        y (int): Second integer.

    Returns:
        int: Hamming distance.
    """
    xor = x ^ y
    distance = 0
    while xor:
        distance += 1
        xor &= (xor - 1)
    return distance


if __name__ == "__main__":
    print(f"Hamming distance between 1 and 4: {hamming_distance(1, 4)}")
