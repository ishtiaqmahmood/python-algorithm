def sum_proper_divisors(n):
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i*i != n: s += n // i
    return s


def is_sociable(n, max_len=10):
    """
    Checks if n is a sociable number (part of a sociable cycle).
    """
    curr = n
    seen = []
    for _ in range(max_len):
        curr = sum_proper_divisors(curr)
        if curr == n: return True
        if curr in seen or curr == 1: return False
        seen.append(curr)
    return False


if __name__ == "__main__":
    print(f"Is 12496 sociable? {is_sociable(12496)}")
