def find_platforms(arr, dep):
    """
    Finds the minimum number of platforms required at a railway station.

    Args:
        arr (list): Arrival times.
        dep (list): Departure times.

    Returns:
        int: Minimum platforms.
    """
    arr.sort()
    dep.sort()

    n = len(arr)
    platforms = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        result = max(result, platforms)

    return result


if __name__ == "__main__":
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    print(f"Min platforms needed: {find_platforms(arrival, departure)}")
