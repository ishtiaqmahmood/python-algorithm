def has_cycle(head):
    """
    Detects cycle in a linked list using Floyd's Cycle-Finding Algorithm.

    Args:
        head (Node): Head of the linked list.

    Returns:
        bool: True if cycle exists, False otherwise.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3
    n3.next = n1 # cycle
    print(f"Has cycle: {has_cycle(n1)}")
    n3.next = None
    print(f"Has cycle after removal: {has_cycle(n1)}")
