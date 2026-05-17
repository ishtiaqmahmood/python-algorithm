class Deque:
    """
    Implementation of a double-ended queue (Deque).
    """
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0) if self.items else None

    def remove_rear(self):
        return self.items.pop() if self.items else None

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    d = Deque()
    d.add_rear(4)
    d.add_rear(8)
    d.add_front(6)
    print(f"Front removed: {d.remove_front()}")
    print(f"Rear removed: {d.remove_rear()}")
