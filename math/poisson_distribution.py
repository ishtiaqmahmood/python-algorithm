import math


def poisson_pmf(k, lambd):
    """
    Probability Mass Function of Poisson Distribution.
    """
    return (lambd**k * math.exp(-lambd)) / math.factorial(k)


if __name__ == "__main__":
    print(f"Poisson PMF (k=3, lambda=5): {poisson_pmf(3, 5)}")
