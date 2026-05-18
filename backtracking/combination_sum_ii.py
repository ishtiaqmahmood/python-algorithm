def combination_sum_ii(candidates, target):
    """
    Combination Sum II (Each number used once).
    """
    res = []
    candidates.sort()

    def backtrack(remain, path, start):
        if remain == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]: continue
            if candidates[i] > remain: break
            path.append(candidates[i])
            backtrack(remain - candidates[i], path, i + 1)
            path.pop()

    backtrack(target, [], 0)
    return res


if __name__ == "__main__":
    print(f"Combos for 8: {combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)}")
