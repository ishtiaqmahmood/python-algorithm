def read_binary_watch(turned_on):
    """
    Binary Watch (all possible times).
    """
    res = []
    for h in range(12):
        for m in range(60):
            if (bin(h).count('1') + bin(m).count('1')) == turned_on:
                res.append(f"{h}:{m:02d}")
    return res


if __name__ == "__main__":
    print(f"Watch times (1 bit): {read_binary_watch(1)}")
