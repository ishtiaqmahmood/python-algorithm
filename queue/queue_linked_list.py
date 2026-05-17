class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    """
    A class to represent a linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Queue:
    """
    A class to represent a queue using a linked list.
    """
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        Args:
            value: The value to be added.
        """
        new_node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.linked_list.head is None

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
            Node: The node removed from the front.
        """
        if self.is_empty():
            return "There is not any node in the Queue"
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            return temp_node

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            Node: The node at the front.
        """
        if self.is_empty():
            return "There is not any node in the Queue"
        else:
            return self.linked_list.head

    def delete(self):
        """
        Deletes the entire queue.
        """
        self.linked_list.head = None
        self.linked_list.tail = None


if __name__ == "__main__":
    cust_queue = Queue()
    cust_queue.enqueue(1)
    cust_queue.enqueue(2)
    cust_queue.enqueue(3)
    cust_queue.enqueue(4)
    print(cust_queue)
    cust_queue.dequeue()
    print(cust_queue)
    cust_queue.delete()
    print(f"Queue after delete: {cust_queue}")
