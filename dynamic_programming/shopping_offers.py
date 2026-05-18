def shopping_offers(price, special, needs):
    """
    Shopping Offers.
    """
    memo = {}

    def solve(cur_needs):
        state = tuple(cur_needs)
        if state in memo: return memo[state]

        # Default price without any special offers
        res = sum(cur_needs[i] * price[i] for i in range(len(needs)))

        for offer in special:
            new_needs = []
            for i in range(len(needs)):
                if offer[i] > cur_needs[i]:
                    break
                new_needs.append(cur_needs[i] - offer[i])
            else:
                res = min(res, offer[-1] + solve(new_needs))

        memo[state] = res
        return res

    return solve(needs)


if __name__ == "__main__":
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    print(f"Min cost: {shopping_offers(price, special, needs)}")
