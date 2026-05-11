def power(base, exp):
    """
    Computes the power of a number.

    Args:
        base (int or float): The base number.
        exp (int): The non-negative integer exponent.

    Returns:
        int or float: The result of base raised to the power of exp.
    """
    assert exp >= 0 and int(exp) == exp, 'The exponent must be positive integer'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp - 1)

if __name__ == "__main__":
    test_base = 2
    test_exp = 4
    print(f"{test_base} raised to the power of {test_exp} is {power(test_base, test_exp)}")
