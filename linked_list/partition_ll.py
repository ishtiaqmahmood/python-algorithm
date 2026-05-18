class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    """
    Partitions a linked list such that all nodes less than x come before nodes
    greater than or equal to x.

    Args:
        head (ListNode): Head of list.
        x (int): Partition value.

    Returns:
        ListNode: Partitioned list head.
    """
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    after.next = None
    before.next = after_head.next
    return before_head.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    head = partition(head, 3)
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
