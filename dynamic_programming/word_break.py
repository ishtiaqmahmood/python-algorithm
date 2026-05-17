def word_break(s, word_dict):
    """
    Determines if a string can be segmented into a space-separated sequence of one or more dictionary words.

    Args:
        s (str): The string to segment.
        word_dict (list): List of allowed words.

    Returns:
        bool: True if it can be segmented, False otherwise.
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    word_set = set(word_dict)

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    test_str = "leetcode"
    test_dict = ["leet", "code"]
    print(f"Word break for '{test_str}' with {test_dict}: {word_break(test_str, test_dict)}")
