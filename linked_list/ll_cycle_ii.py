class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle_ii(head):
    """
    Returns the node where the cycle begins. If there is no cycle, returns None.

    Args:
        head (ListNode): Head of list.

    Returns:
        ListNode: Start of cycle.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    ptr1 = head
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1


if __name__ == "__main__":
    head = ListNode(3)
    node2 = ListNode(2)
    head.next = node2
    node2.next = ListNode(0)
    node2.next.next = ListNode(-4)
    node2.next.next.next = node2  # cycle
    res = detect_cycle_ii(head)
    print(f"Cycle starts at node with value: {res.val if res else None}")
