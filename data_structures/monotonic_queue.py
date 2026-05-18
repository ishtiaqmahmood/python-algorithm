from collections import deque


class MonotonicQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, val):
        while self.queue and self.queue[-1] < val:
            self.queue.pop()
        self.queue.append(val)

    def max(self):
        return self.queue[0]

    def pop(self, val):
        if self.queue and self.queue[0] == val:
            self.queue.popleft()


if __name__ == "__main__":
    mq = MonotonicQueue()
    mq.push(1); mq.push(3); mq.push(-1)
    print(f"Max: {mq.max()}")
