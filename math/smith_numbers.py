def sum_digits(n):
    return sum(int(d) for d in str(n))


def get_prime_factors(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1: factors.append(temp)
    return factors


def is_smith(n):
    """
    Checks if n is a Smith number.
    Sum of digits = sum of digits of its prime factors.
    """
    if is_prime(n): return False
    factors = get_prime_factors(n)
    sum_f = sum(sum_digits(f) for f in factors)
    return sum_digits(n) == sum_f


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True


if __name__ == "__main__":
    print(f"Is 666 Smith? {is_smith(666)}")
    print(f"Is 4 Smith? {is_smith(4)}")
