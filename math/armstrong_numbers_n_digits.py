def is_armstrong_n(n):
    """
    Checks if n is an Armstrong number of any digit length.
    """
    s = str(n)
    k = len(s)
    return sum(int(d)**k for d in s) == n


if __name__ == "__main__":
    print(f"Is 153 Armstrong? {is_armstrong_n(153)}")
    print(f"Is 1634 Armstrong? {is_armstrong_n(1634)}")
