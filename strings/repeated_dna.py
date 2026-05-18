def find_repeated_dna_sequences(s):
    """
    Finds all 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

    Args:
        s (str): DNA sequence.

    Returns:
        list: Repeated sequences.
    """
    seen = set()
    res = set()
    for i in range(len(s) - 9):
        ten = s[i:i+10]
        if ten in seen:
            res.add(ten)
        seen.add(ten)
    return list(res)


if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(f"Repeated DNA: {find_repeated_dna_sequences(s)}")
