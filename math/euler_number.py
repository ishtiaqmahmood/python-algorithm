def calculate_e(terms):
    """
    Calculates Euler's number 'e' using the infinite series:
    e = 1/0! + 1/1! + 1/2! + 1/3! + ...

    Args:
        terms (int): Number of terms.

    Returns:
        float: Calculated value of e.
    """
    e = 0
    fact = 1
    for i in range(terms):
        if i > 0:
            fact *= i
        e += 1 / fact
    return e


if __name__ == "__main__":
    print(f"e (15 terms): {calculate_e(15)}")
    import math
    print(f"Actual e: {math.exp(1)}")
