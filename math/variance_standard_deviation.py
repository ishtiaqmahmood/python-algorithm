import math


def variance(data):
    m = sum(data) / len(data)
    return sum((x - m)**2 for x in data) / len(data)


def standard_deviation(data):
    return math.sqrt(variance(data))


if __name__ == "__main__":
    data = [10, 12, 23, 23, 16, 23, 21, 16]
    print(f"Variance: {variance(data)}")
    print(f"Std Dev: {standard_deviation(data)}")
