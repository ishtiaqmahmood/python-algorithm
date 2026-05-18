class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head):
    """
    Returns the middle node of the linked list.

    Args:
        head (ListNode): Head of list.

    Returns:
        ListNode: Middle node.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    mid = middle_node(head)
    print(f"Middle node value: {mid.val}")
