def count_and_say(n):
    """
    Generates the nth term in the count-and-say sequence.

    Args:
        n (int): Term index.

    Returns:
        str: nth term.
    """
    if n == 1:
        return "1"

    prev = count_and_say(n - 1)
    res = ""
    i = 0
    while i < len(prev):
        count = 1
        while i + 1 < len(prev) and prev[i] == prev[i + 1]:
            i += 1
            count += 1
        res += str(count) + prev[i]
        i += 1
    return res


if __name__ == "__main__":
    for i in range(1, 6):
        print(f"CountAndSay({i}) = {count_and_say(i)}")
