def stirling_first_kind(n, k):
    """
    Stirling numbers of the first kind (signed).
    s(n, k) = s(n-1, k-1) - (n-1)*s(n-1, k)
    """
    if n == k == 0: return 1
    if n == 0 or k == 0: return 0
    if n == k: return 1
    return stirling_first_kind(n-1, k-1) - (n-1)*stirling_first_kind(n-1, k)


if __name__ == "__main__":
    print(f"s(4, 2) = {stirling_first_kind(4, 2)}")
