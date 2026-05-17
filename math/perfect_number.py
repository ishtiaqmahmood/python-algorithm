def is_perfect(n):
    """
    Checks if a number is a perfect number.

    Args:
        n (int): Input number.

    Returns:
        bool: True if perfect, False otherwise.
    """
    if n <= 1:
        return False
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if i * i != n:
                sum_div += n // i
    return sum_div == n


if __name__ == "__main__":
    print(f"Is 28 perfect? {is_perfect(28)}")
    print(f"Is 10 perfect? {is_perfect(10)}")
