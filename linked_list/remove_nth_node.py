class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    """
    Removes the nth node from the end of the list.

    Args:
        head (ListNode): Head of list.
        n (int): Position from end.

    Returns:
        ListNode: New head of list.
    """
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = remove_nth_from_end(head, 2)
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
