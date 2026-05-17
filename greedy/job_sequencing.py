def job_sequencing(jobs):
    """
    Finds the maximum profit by sequencing jobs with deadlines.

    Args:
        jobs (list): List of tuples (job_id, deadline, profit).

    Returns:
        tuple: (Total profit, Sequence of jobs)
    """
    # Sort by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    result = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:
        # Check from deadline backwards for a free slot
        for j in range(min(max_deadline, deadline) - 1, -1, -1):
            if result[j] is None:
                result[j] = job_id
                total_profit += profit
                break

    return total_profit, [job for job in result if job is not None]


if __name__ == "__main__":
    job_list = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
    profit, sequence = job_sequencing(job_list)
    print(f"Max Profit: {profit}, Sequence: {sequence}")
