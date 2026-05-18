import bisect


def job_scheduling(start_time, end_time, profit):
    """
    Maximum Profit in Job Scheduling.
    """
    jobs = sorted(zip(start_time, end_time, profit), key=lambda x: x[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect_right(dp, [s, float('inf')]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]


if __name__ == "__main__":
    s = [1, 2, 3, 3]; e = [3, 4, 5, 6]; p = [50, 10, 40, 70]
    print(f"Max job profit: {job_scheduling(s, e, p)}")
