class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    """
    A class to represent a linked list.
    """
    def __init__(self):
        self.head = None

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Stack:
    """
    A class to represent a stack using a linked list.
    """
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return '\n'.join(values)

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.linked_list.head is None

    def push(self, value):
        """
        Adds an element to the top of the stack.

        Args:
            value: The value to be added.
        """
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Returns:
            The value removed from the top.
        """
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            node_value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return node_value

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            The value at the top.
        """
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            node_value = self.linked_list.head.value
            return node_value

    def delete(self):
        """
        Deletes the entire stack.
        """
        self.linked_list.head = None


if __name__ == "__main__":
    custom_stack = Stack()
    custom_stack.push(1)
    custom_stack.push(2)
    custom_stack.push(3)
    print(custom_stack)
    print("-------")
    custom_stack.pop()
    print(custom_stack)
    print("-------")
    print(f"Peek: {custom_stack.peek()}")
