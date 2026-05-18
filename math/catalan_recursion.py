def catalan(n):
    """
    Calculates nth Catalan number using recursion.
    """
    if n <= 1: return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)
    return res


if __name__ == "__main__":
    for i in range(6):
        print(f"C({i}) = {catalan(i)}")
