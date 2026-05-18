class NestedIterator:
    """
    Flattens a nested list iterator.
    """
    def __init__(self, nested_list):
        self.queue = []
        self._flatten(nested_list)

    def _flatten(self, nested):
        for i in nested:
            if isinstance(i, int):
                self.queue.append(i)
            else:
                self._flatten(i)

    def next(self):
        return self.queue.pop(0)

    def has_next(self):
        return len(self.queue) > 0


if __name__ == "__main__":
    nested = [[1, 1], 2, [1, 1]]
    it = NestedIterator(nested)
    res = []
    while it.has_next():
        res.append(it.next())
    print(f"Flattened: {res}")
