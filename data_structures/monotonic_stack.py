class MonotonicStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        while self.stack and self.stack[-1] < val:
            self.stack.pop()
        self.stack.append(val)


if __name__ == "__main__":
    ms = MonotonicStack()
    for x in [2, 1, 5, 6, 2, 3]:
        ms.push(x)
    print(f"Stack: {ms.stack}")
