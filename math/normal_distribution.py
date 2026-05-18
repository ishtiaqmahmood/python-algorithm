import math


def normal_pdf(x, mu, sigma):
    """
    Probability Density Function of Normal Distribution.
    """
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma)**2)


if __name__ == "__main__":
    print(f"Normal PDF (0, 0, 1): {normal_pdf(0, 0, 1)}")
