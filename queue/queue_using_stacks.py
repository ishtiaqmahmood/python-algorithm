class MyQueue:
    """
    Implementation of a queue using two stacks.
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1] if self.s2 else None

    def empty(self):
        return not self.s1 and not self.s2

if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(f"Peek: {q.peek()}")
    print(f"Pop: {q.pop()}")
    print(f"Empty: {q.empty()}")
