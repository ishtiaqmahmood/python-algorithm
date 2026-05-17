class Stack:
    """
    A class to represent a stack using a Python list.
    """
    def __init__(self):
        self.list = []

    def __str__(self):
        if self.list is None:
            return ""
        # Create a copy and reverse it for display
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

    def push(self, value):
        """
        Adds an element to the top of the stack.

        Args:
            value: The value to be added.

        Returns:
            str: A success message.
        """
        self.list.append(value)
        return "The element is successfully inserted"

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Returns:
            The value removed from the top.
        """
        if self.is_empty():
            return "There is not any element in the Stack"
        else:
            return self.list.pop()

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            The value at the top.
        """
        if self.is_empty():
            return "There is not any element in the Stack"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        """
        Deletes the entire stack.
        """
        self.list = []


if __name__ == "__main__":
    custom_stack = Stack()
    custom_stack.push(1)
    custom_stack.push(2)
    custom_stack.push(3)
    print(f"Popped: {custom_stack.pop()}")
    print(f"Peek: {custom_stack.peek()}")
    print("Stack contents:")
    print(custom_stack)
    custom_stack.delete()
    print(f"Stack after delete: {custom_stack}")
