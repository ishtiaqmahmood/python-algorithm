def partition(s):
    """
    Palindrome Partitioning (Backtracking).
    """
    res = []

    def is_palindrome(sub): return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            res.append(list(path))
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return res


if __name__ == "__main__":
    print(f"Partitions of 'aab': {partition('aab')}")
