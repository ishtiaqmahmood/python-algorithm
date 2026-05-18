def is_palindrome(s):
    return s == s[::-1]


def palindrome_pairs(words):
    """
    Finds all pairs of indices such that words[i] + words[j] is a palindrome.

    Args:
        words (list): List of strings.

    Returns:
        list: List of pairs of indices.
    """
    res = []
    word_to_id = {word: i for i, word in enumerate(words)}
    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            if is_palindrome(prefix):
                back = suffix[::-1]
                if back in word_to_id and word_to_id[back] != i:
                    res.append([word_to_id[back], i])
            if j != len(word) and is_palindrome(suffix):
                back = prefix[::-1]
                if back in word_to_id and word_to_id[back] != i:
                    res.append([i, word_to_id[back]])
    return res


if __name__ == "__main__":
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(f"Palindrome pairs: {palindrome_pairs(words)}")
