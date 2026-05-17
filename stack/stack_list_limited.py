class Stack:
    """
    A class to represent a stack with a maximum capacity.
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return '\n'.join(values)

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.list == []

    def is_full(self):
        """
        Checks if the stack is full.

        Returns:
            bool: True if full, False otherwise.
        """
        return len(self.list) == self.max_size

    def push(self, value):
        """
        Adds an element to the top of the stack if it's not full.

        Args:
            value: The value to be added.

        Returns:
            str: A message indicating the result.
        """
        if self.is_full():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Returns:
            The value removed from the top.
        """
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            The value at the top.
        """
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        """
        Deletes the entire stack.
        """
        self.list = []


if __name__ == "__main__":
    custom_stack = Stack(4)
    print(f"Is empty: {custom_stack.is_empty()}")
    print(f"Is full: {custom_stack.is_full()}")
    custom_stack.push(1)
    custom_stack.push(2)
    custom_stack.push(3)
    print(custom_stack)
