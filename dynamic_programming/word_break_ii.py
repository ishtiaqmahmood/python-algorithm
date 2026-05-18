def word_break(s, wordDict):
    """
    Word Break II.
    """
    memo = {}
    word_set = set(wordDict)

    def dfs(s):
        if not s: return [""]
        if s in memo: return memo[s]

        res = []
        for word in word_set:
            if s.startswith(word):
                sub_sentences = dfs(s[len(word):])
                for sub in sub_sentences:
                    res.append(word + ("" if not sub else " " + sub))

        memo[s] = res
        return res

    return dfs(s)


if __name__ == "__main__":
    s = "catsanddog"
    words = ["cat", "cats", "and", "sand", "dog"]
    print(f"Word break combinations: {word_break(s, words)}")
