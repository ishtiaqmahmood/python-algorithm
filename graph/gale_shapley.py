def gale_shapley(men_prefs, women_prefs):
    """
    Gale-Shapley algorithm for the Stable Marriage Problem.

    Args:
        men_prefs (dict): Preferences of men.
        women_prefs (dict): Preferences of women.

    Returns:
        dict: Stable matching.
    """
    n = len(men_prefs)
    free_men = list(men_prefs.keys())
    engaged_to = {}  # woman -> man
    proposals = {man: 0 for man in free_men}

    while free_men:
        man = free_men.pop(0)
        man_pref_list = men_prefs[man]
        woman = man_pref_list[proposals[man]]
        proposals[man] += 1

        if woman not in engaged_to:
            engaged_to[woman] = man
        else:
            current_man = engaged_to[woman]
            woman_pref_list = women_prefs[woman]
            if woman_pref_list.index(man) < woman_pref_list.index(current_man):
                engaged_to[woman] = man
                free_men.append(current_man)
            else:
                free_men.append(man)
    return engaged_to


if __name__ == "__main__":
    men_prefs = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'X', 'Z'],
        'C': ['X', 'Y', 'Z']
    }
    women_prefs = {
        'X': ['B', 'A', 'C'],
        'Y': ['A', 'B', 'C'],
        'Z': ['A', 'B', 'C']
    }
    print(f"Stable Matching: {gale_shapley(men_prefs, women_prefs)}")
