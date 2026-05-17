class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    """
    Implementation of a Circular Doubly Linked List.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return
        last = self.head.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    def display(self):
        if not self.head: return
        elements = []
        curr = self.head
        while True:
            elements.append(str(curr.data))
            curr = curr.next
            if curr == self.head: break
        print(" <-> ".join(elements) + " <-> (head)")

if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    cdll.append(1)
    cdll.append(2)
    cdll.append(3)
    cdll.display()
