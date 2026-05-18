from collections import Counter


def mean(data):
    return sum(data) / len(data)


def median(data):
    n = len(data)
    s = sorted(data)
    if n % 2 == 0:
        return (s[n//2 - 1] + s[n//2]) / 2
    else:
        return s[n//2]


def mode(data):
    c = Counter(data)
    m = max(c.values())
    return [k for k, v in c.items() if v == m]


if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5, 5]
    print(f"Mean: {mean(data)}, Median: {median(data)}, Mode: {mode(data)}")
