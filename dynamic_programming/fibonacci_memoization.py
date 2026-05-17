def fib_memo(n, memo=None):
    """
    Calculates the nth Fibonacci number using memoization (Top-Down DP).

    Args:
        n (int): The position in the Fibonacci sequence.
        memo (dict): Dictionary to store already computed values.

    Returns:
        int: The nth Fibonacci number.
    """
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(f"Fibonacci(10) with memoization: {fib_memo(10)}")
    print(f"Fibonacci(50) with memoization: {fib_memo(50)}")
