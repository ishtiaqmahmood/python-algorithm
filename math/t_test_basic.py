import math


def t_test_basic(sample1, sample2):
    """
    Simple independent t-test conceptual structure.
    """
    m1, m2 = sum(sample1)/len(sample1), sum(sample2)/len(sample2)
    s1 = sum((x - m1)**2 for x in sample1) / (len(sample1) - 1)
    s2 = sum((x - m2)**2 for x in sample2) / (len(sample2) - 1)

    t_stat = (m1 - m2) / math.sqrt(s1/len(sample1) + s2/len(sample2))
    return t_stat


if __name__ == "__main__":
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 3, 4, 5, 6]
    print(f"T-statistic: {t_test_basic(s1, s2)}")
