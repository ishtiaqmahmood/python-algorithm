def combination_sum(candidates, target):
    """
    Combination Sum (all unique combinations that sum to target).
    """
    res = []
    candidates.sort()

    def backtrack(remain, path, start):
        if remain == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain: break
            path.append(candidates[i])
            backtrack(remain - candidates[i], path, i)
            path.pop()

    backtrack(target, [], 0)
    return res


if __name__ == "__main__":
    print(f"Combos for 7: {combination_sum([2, 3, 6, 7], 7)}")
