class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    """
    Reorders a linked list as L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

    Args:
        head (ListNode): Head of list.
    """
    if not head:
        return

    # 1. find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. reverse second half
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # 3. merge
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder_list(head)
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
