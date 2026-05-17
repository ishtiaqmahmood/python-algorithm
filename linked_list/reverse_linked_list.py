def reverse_linked_list(head):
    """
    Reverses a singly linked list.

    Args:
        head (Node): Head of the linked list.

    Returns:
        Node: New head of the reversed list.
    """
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display(head):
    elements = []
    while head:
        elements.append(str(head.data))
        head = head.next
    print(" -> ".join(elements))

if __name__ == "__main__":
    h = Node(1)
    h.next = Node(2)
    h.next.next = Node(3)
    print("Original:")
    display(h)
    h = reverse_linked_list(h)
    print("Reversed:")
    display(h)
