def kaprekar_step(n):
    s = str(n).zfill(4)
    asc = "".join(sorted(s))
    desc = asc[::-1]
    return int(desc) - int(asc)


def get_kaprekar_routine(n):
    """
    Computes the sequence of numbers leading to the Kaprekar's constant (6174).
    The routine works for 4-digit numbers with at least two different digits.

    Args:
        n (int): 4-digit number.

    Returns:
        list: Sequence of numbers.
    """
    if len(set(str(n).zfill(4))) < 2:
        return []

    res = [n]
    while n != 6174:
        n = kaprekar_step(n)
        res.append(n)
    return res


if __name__ == "__main__":
    n = 1234
    print(f"Kaprekar routine for {n}: {get_kaprekar_routine(n)}")
