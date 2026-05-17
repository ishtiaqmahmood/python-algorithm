def police_thieves(arr, k):
    """
    Finds the maximum number of thieves that can be caught.

    Args:
        arr (list): List of 'P' (Police) and 'T' (Thief).
        k (int): Maximum distance a policeman can catch a thief.

    Returns:
        int: Number of thieves caught.
    """
    n = len(arr)
    police = []
    thieves = []
    for i in range(n):
        if arr[i] == 'P':
            police.append(i)
        else:
            thieves.append(i)

    i = j = caught = 0
    while i < len(police) and j < len(thieves):
        if abs(police[i] - thieves[j]) <= k:
            caught += 1
            i += 1
            j += 1
        elif police[i] < thieves[j]:
            i += 1
        else:
            j += 1
    return caught


if __name__ == "__main__":
    test_arr = ['P', 'T', 'T', 'P', 'T']
    dist = 1
    print(f"Thieves caught: {police_thieves(test_arr, dist)}")
