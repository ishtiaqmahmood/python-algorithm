def next_permutation(p):
    n = len(p)
    i = n - 2
    while i >= 0 and p[i] >= p[i+1]: i -= 1
    if i == -1: return None
    j = n - 1
    while p[j] <= p[i]: j -= 1
    p[i], p[j] = p[j], p[i]
    p[i+1:] = reversed(p[i+1:])
    return p


def all_permutations(n):
    """
    Generates all permutations of {1, ..., n} in lexicographical order.
    """
    p = list(range(1, n + 1))
    res = []
    while p:
        res.append(list(p))
        p = next_permutation(p)
    return res


if __name__ == "__main__":
    print(f"Permutations of 3: {all_permutations(3)}")
