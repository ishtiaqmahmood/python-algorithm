def square_root(n, precision=0.0001):
    """
    Calculates the square root of a number using Newton's method.

    Args:
        n (float): Input number.
        precision (float): Desired precision.

    Returns:
        float: Square root of n.
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    x = n
    while True:
        root = 0.5 * (x + (n / x))
        if abs(root - x) < precision:
            return root
        x = root


if __name__ == "__main__":
    print(f"Square root of 2: {square_root(2)}")
