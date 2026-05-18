def combination_sum_iii(k, n):
    """
    Combination Sum III (k numbers from 1-9 sum to n).
    """
    res = []

    def backtrack(remain, path, start):
        if len(path) == k:
            if remain == 0: res.append(list(path))
            return
        for i in range(start, 10):
            if i > remain: break
            path.append(i)
            backtrack(remain - i, path, i + 1)
            path.pop()

    backtrack(n, [], 1)
    return res


if __name__ == "__main__":
    print(f"3 numbers sum to 7: {combination_sum_iii(3, 7)}")
