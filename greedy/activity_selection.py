def activity_selection(start_times, end_times):
    """
    Selects the maximum number of activities that don't overlap.

    Args:
        start_times (list): Start times of activities.
        end_times (list): End times of activities.

    Returns:
        list: Indices of selected activities.
    """
    activities = []
    for i in range(len(start_times)):
        activities.append((start_times[i], end_times[i], i))

    # Sort by end time
    activities.sort(key=lambda x: x[1])

    result = []
    if not activities:
        return result

    # Select the first activity
    result.append(activities[0][2])
    last_end_time = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            result.append(activities[i][2])
            last_end_time = activities[i][1]

    return result


if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    e = [2, 4, 6, 7, 9, 9]
    print(f"Selected activities: {activity_selection(s, e)}")
