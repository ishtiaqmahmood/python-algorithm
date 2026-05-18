class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def has_cycle_dll(head):
    """
    Detects cycle in a doubly linked list.

    Args:
        head (ListNode): Head of list.

    Returns:
        bool: True if cycle exists.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    head = ListNode(1)
    node2 = ListNode(2)
    head.next = node2
    node2.prev = head
    node2.next = head  # cycle
    head.prev = node2
    print(f"Has cycle? {has_cycle_dll(head)}")
