import heapq

class PriorityQueue:
    """
    Implementation of a Priority Queue using heapq.
    """
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("task1", 3)
    pq.push("task2", 1)
    pq.push("task3", 2)
    print(f"Popped: {pq.pop()}")
    print(f"Popped: {pq.pop()}")
