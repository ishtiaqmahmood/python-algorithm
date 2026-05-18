def matrix_inverse(m):
    """
    Calculates the inverse of a 2x2 matrix.
    """
    det = m[0][0]*m[1][1] - m[0][1]*m[1][0]
    if det == 0: return None
    return [
        [m[1][1]/det, -m[0][1]/det],
        [-m[1][0]/det, m[0][0]/det]
    ]


if __name__ == "__main__":
    m = [[4, 7], [2, 6]]
    print(f"Inverse: {matrix_inverse(m)}")
