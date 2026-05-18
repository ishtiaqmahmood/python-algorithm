def euler_totient(n):
    """
    Computes Euler's Totient function φ(n), which counts the number of
    integers up to n that are relatively prime to n.

    Args:
        n (int): Input number.

    Returns:
        int: φ(n)
    """
    result = n
    p = 2
    temp_n = n
    while p * p <= temp_n:
        if temp_n % p == 0:
            while temp_n % p == 0:
                temp_n //= p
            result -= result // p
        p += 1
    if temp_n > 1:
        result -= result // temp_n
    return result


if __name__ == "__main__":
    for i in range(1, 11):
        print(f"φ({i}) = {euler_totient(i)}")
