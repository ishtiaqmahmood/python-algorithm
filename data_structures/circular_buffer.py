class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            self.head = (self.head + 1) % self.size
        else:
            self.count += 1
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.count == 0: return None
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item


if __name__ == "__main__":
    cb = CircularBuffer(3)
    cb.enqueue(1); cb.enqueue(2); cb.enqueue(3); cb.enqueue(4)
    print(f"Dequeue: {cb.dequeue()}") # Should be 2 because 1 was overwritten by 4
