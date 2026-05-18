def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    """
    Calculates P(A|B) using Bayes' Theorem.
    """
    p_not_a = 1 - p_a
    p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a
    return (p_b_given_a * p_a) / p_b


if __name__ == "__main__":
    # P(Cancer) = 0.01, P(Pos|Cancer) = 0.9, P(Pos|No Cancer) = 0.05
    print(f"P(Cancer|Pos): {bayes_theorem(0.01, 0.9, 0.05)}")
