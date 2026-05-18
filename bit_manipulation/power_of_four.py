def is_power_of_four(n):
    """
    Checks if a number is a power of four.
    """
    return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0


if __name__ == "__main__":
    for i in [16, 8, 1]:
        print(f"Is {i} power of 4? {is_power_of_four(i)}")
