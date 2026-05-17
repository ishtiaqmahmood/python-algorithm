class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    """
    Implementation of a Circular Singly Linked List.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head: return
        elements = []
        curr = self.head
        while True:
            elements.append(str(curr.data))
            curr = curr.next
            if curr == self.head: break
        print(" -> ".join(elements) + " -> (head)")

if __name__ == "__main__":
    cll = CircularSinglyLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.display()
