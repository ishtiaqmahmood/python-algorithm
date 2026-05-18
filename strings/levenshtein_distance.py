def levenshtein_distance(s1, s2):
    """
    Calculates the Levenshtein distance between two strings.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        int: Levenshtein distance.
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if not s2:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


if __name__ == "__main__":
    s1, s2 = "kitten", "sitting"
    print(f"Levenshtein distance between '{s1}' and '{s2}': {levenshtein_distance(s1, s2)}")
