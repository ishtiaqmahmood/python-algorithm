def collatz_sequence(n):
    """
    Generates the Collatz sequence for a positive integer n.
    The sequence is defined as: if n is even, next is n/2; if n is odd, next is 3n+1.
    The conjecture is that the sequence always reaches 1.

    Args:
        n (int): Starting number.

    Returns:
        list: Collatz sequence.
    """
    if n <= 0:
        return []
    res = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        res.append(n)
    return res


if __name__ == "__main__":
    n = 6
    print(f"Collatz sequence for {n}: {collatz_sequence(n)}")
