def is_narcissistic(n):
    """
    Narcissistic number is same as Armstrong number.
    """
    s = str(n)
    k = len(s)
    return sum(int(d)**k for d in s) == n


if __name__ == "__main__":
    print(f"Is 370 narcissistic? {is_narcissistic(370)}")
