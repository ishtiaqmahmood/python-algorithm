def string_hash(s, p=31, m=10**9 + 9):
    """
    Calculates the polynomial rolling hash of a string.

    Args:
        s (str): Input string.
        p (int): Base prime.
        m (int): Modulo.

    Returns:
        int: Hash value.
    """
    hash_value = 0
    p_pow = 1
    for char in s:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value


if __name__ == "__main__":
    s1, s2 = "abc", "abd"
    print(f"Hash of '{s1}': {string_hash(s1)}")
    print(f"Hash of '{s2}': {string_hash(s2)}")
