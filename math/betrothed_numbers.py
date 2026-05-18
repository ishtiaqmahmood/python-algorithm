def sum_proper_divisors(n):
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i*i != n: s += n // i
    return s


def are_betrothed(a, b):
    """
    Checks if two numbers are betrothed (quasi-amicable).
    """
    return sum_proper_divisors(a) == b + 1 and sum_proper_divisors(b) == a + 1


if __name__ == "__main__":
    print(f"Are 48 and 75 betrothed? {are_betrothed(48, 75)}")
