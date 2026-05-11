class Queue:
    """
    A class to represent a circular queue with a fixed capacity.
    """
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_full(self):
        """
        Checks if the queue is full.

        Returns:
            bool: True if full, False otherwise.
        """
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.top == -1

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        Args:
            value: The value to be added.

        Returns:
            str: A message indicating the result.
        """
        if self.is_full():
            return "The queue is full"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The value removed from the front.
        """
        if self.is_empty():
            return "There is not any element in the Queue"
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            The value at the front.
        """
        if self.is_empty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]

    def delete(self):
        """
        Deletes the entire queue.
        """
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1


if __name__ == "__main__":
    custom_queue = Queue(3)
    custom_queue.enqueue(1)
    custom_queue.enqueue(2)
    custom_queue.enqueue(3)
    print(custom_queue)
    custom_queue.dequeue()
    custom_queue.enqueue(4)
    print(custom_queue)
    custom_queue.dequeue()
    print(custom_queue)
