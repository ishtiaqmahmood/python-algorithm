def can_cross(stones):
    """
    Frog Jump.
    """
    stone_set = set(stones)
    memo = set()

    def solve(pos, k):
        if pos == stones[-1]:
            return True
        if (pos, k) in memo:
            return False

        for jump in range(k - 1, k + 2):
            if jump > 0 and (pos + jump) in stone_set:
                if solve(pos + jump, jump):
                    return True

        memo.add((pos, k))
        return False

    return solve(stones[0], 0)


if __name__ == "__main__":
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    print(f"Can frog cross? {can_cross(stones)}")
