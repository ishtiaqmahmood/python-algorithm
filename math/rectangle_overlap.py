def is_rectangle_overlap(rec1, rec2):
    """
    Checks if two rectangles overlap.
    Rectangles are represented as [x1, y1, x2, y2].

    Args:
        rec1 (list): First rectangle.
        rec2 (list): Second rectangle.

    Returns:
        bool: True if they overlap, False otherwise.
    """
    return not (rec1[2] <= rec2[0] or  # left
                rec1[0] >= rec2[2] or  # right
                rec1[1] >= rec2[3] or  # top
                rec1[3] <= rec2[1])    # bottom


if __name__ == "__main__":
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    print(f"Do they overlap? {is_rectangle_overlap(rec1, rec2)}")
