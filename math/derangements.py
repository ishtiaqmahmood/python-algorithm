def count_derangements(n):
    """
    Counts the number of derangements of n elements (subfactorial).
    """
    if n == 0: return 1
    if n == 1: return 0

    a, b = 1, 0
    for i in range(2, n + 1):
        a, b = b, (i - 1) * (a + b)
    return b


if __name__ == "__main__":
    for i in range(6):
        print(f"!{i} = {count_derangements(i)}")
