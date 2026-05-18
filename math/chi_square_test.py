def chi_square_test(observed, expected):
    """
    Calculates Chi-square statistic.
    """
    return sum((o - e)**2 / e for o, e in zip(observed, expected))


if __name__ == "__main__":
    obs = [16, 18, 16, 14, 12, 12]
    exp = [14.66] * 6
    print(f"Chi-square: {chi_square_test(obs, exp)}")
