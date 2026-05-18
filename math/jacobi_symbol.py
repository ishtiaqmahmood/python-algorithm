def jacobi_symbol(a, n):
    """
    Computes the Jacobi symbol (a/n).
    """
    if n <= 0 or n % 2 == 0: return 0
    a %= n
    res = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


if __name__ == "__main__":
    print(f"Jacobi symbol (5, 9): {jacobi_symbol(5, 9)}")
