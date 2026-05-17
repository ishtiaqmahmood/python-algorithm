def fib_tab(n):
    """
    Calculates the nth Fibonacci number using tabulation (Bottom-Up DP).

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    tb = [0] * (n + 1)
    tb[1] = 1
    for i in range(2, n + 1):
        tb[i] = tb[i - 1] + tb[i - 2]
    return tb[n]


if __name__ == "__main__":
    print(f"Fibonacci(10) with tabulation: {fib_tab(10)}")
    print(f"Fibonacci(50) with tabulation: {fib_tab(50)}")
