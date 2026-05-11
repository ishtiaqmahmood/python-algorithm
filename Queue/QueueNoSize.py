class Queue:
    """
    A class to represent a queue using a Python list (no size limit).
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return not self.items

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        Args:
            value: The value to be added.

        Returns:
            str: A success message.
        """
        self.items.append(value)
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
            return self.items.pop(0)

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            The value at the front.
        """
        if self.is_empty():
            return "There is not any element in the Queue"
        else:
            return self.items[0]

    def delete(self):
        """
        Deletes the entire queue.
        """
        self.items = []


if __name__ == "__main__":
    custom_queue = Queue()
    print(f"Is empty: {custom_queue.is_empty()}")
    custom_queue.enqueue(1)
    custom_queue.enqueue(2)
    custom_queue.enqueue(3)
    print(custom_queue)
    custom_queue.dequeue()
    print(f"Peek: {custom_queue.peek()}")
    print(custom_queue)
    custom_queue.delete()
    print(f"Queue after delete: {custom_queue}")
