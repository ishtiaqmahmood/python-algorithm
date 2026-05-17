def find_divisors(n):
    """
    Finds all divisors of an integer.

    Args:
        n (int): Input integer.

    Returns:
        list: Sorted list of divisors.
    """
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))


if __name__ == "__main__":
    num = 100
    print(f"Divisors of {num}: {find_divisors(num)}")
