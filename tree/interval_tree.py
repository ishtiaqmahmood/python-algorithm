class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high


class IntervalNode:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None


def insert(root, i):
    if not root:
        return IntervalNode(i)

    l = root.interval.low
    if i.low < l:
        root.left = insert(root.left, i)
    else:
        root.right = insert(root.right, i)

    if root.max < i.high:
        root.max = i.high

    return root


def overlap_search(root, i):
    if not root: return None
    if root.interval.low <= i.high and i.low <= root.interval.high:
        return root.interval

    if root.left and root.left.max >= i.low:
        return overlap_search(root.left, i)
    return overlap_search(root.right, i)


if __name__ == "__main__":
    intervals = [Interval(15, 20), Interval(10, 30), Interval(17, 19), Interval(5, 20)]
    root = None
    for i in intervals:
        root = insert(root, i)

    query = Interval(6, 7)
    res = overlap_search(root, query)
    print(f"Overlap with [{query.low}, {query.high}]: [{res.low}, {res.high}] if res else None")
