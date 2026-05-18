def calculate_pi(terms):
    """
    Calculates the value of PI using the Gregory-Leibniz series.
    PI = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

    Args:
        terms (int): Number of terms to use.

    Returns:
        float: Calculated value of PI.
    """
    pi = 0
    denominator = 1
    sign = 1
    for _ in range(terms):
        pi += sign * (4 / denominator)
        denominator += 2
        sign *= -1
    return pi


if __name__ == "__main__":
    print(f"PI (1000 terms): {calculate_pi(1000)}")
    import math
    print(f"Actual PI: {math.pi}")
