def jaro_winkler(s1, s2):
    """
    Calculates the Jaro-Winkler similarity between two strings.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        float: Jaro-Winkler similarity.
    """
    if s1 == s2:
        return 1.0

    len1, len2 = len(s1), len(s2)
    match_distance = max(len1, len2) // 2 - 1
    s1_matches = [False] * len1
    s2_matches = [False] * len2
    matches = 0
    transpositions = 0

    for i in range(len1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len2)
        for j in range(start, end):
            if not s2_matches[j] and s1[i] == s2[j]:
                s1_matches[i] = True
                s2_matches[j] = True
                matches += 1
                break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(len1):
        if s1_matches[i]:
            while not s2_matches[k]:
                k += 1
            if s1[i] != s2[k]:
                transpositions += 1
            k += 1

    jaro = (matches / len1 + matches / len2 + (matches - transpositions / 2) / matches) / 3

    # Winkler modification
    prefix = 0
    for i in range(min(4, len1, len2)):
        if s1[i] == s2[i]:
            prefix += 1
        else:
            break

    return jaro + prefix * 0.1 * (1 - jaro)


if __name__ == "__main__":
    s1, s2 = "MARTHA", "MARHTA"
    print(f"Jaro-Winkler similarity between '{s1}' and '{s2}': {jaro_winkler(s1, s2)}")
