import math


def fib_closed_form(n):
    """
    Calculates the nth Fibonacci number using Binet's Formula.
    F_n = (phi^n - psi^n) / sqrt(5)

    Args:
        n (int): Index.

    Returns:
        int: nth Fibonacci number.
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi**n - psi**n) / math.sqrt(5))


if __name__ == "__main__":
    for i in range(11):
        print(f"F_{i} = {fib_closed_form(i)}")
