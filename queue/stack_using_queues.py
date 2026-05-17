from collections import deque

class MyStack:
    """
    Implementation of a stack using one queue.
    """
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q

if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    print(f"Top: {s.top()}")
    print(f"Pop: {s.pop()}")
    print(f"Empty: {s.empty()}")
