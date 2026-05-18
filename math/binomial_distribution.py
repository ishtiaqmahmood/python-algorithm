import math


def nCr(n, r):
    return math.comb(n, r)


def binomial_pmf(k, n, p):
    """
    Probability Mass Function of Binomial Distribution.
    """
    return nCr(n, k) * (p**k) * ((1 - p)**(n - k))


if __name__ == "__main__":
    print(f"Binomial PMF (k=2, n=10, p=0.5): {binomial_pmf(2, 10, 0.5)}")
