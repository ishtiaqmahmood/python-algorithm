class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head, k):
    """
    Rotates a linked list to the right by k places.

    Args:
        head (ListNode): Head of list.
        k (int): Number of rotations.

    Returns:
        ListNode: Rotated list head.
    """
    if not head:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return head

    curr = head
    for _ in range(length - k - 1):
        curr = curr.next

    new_head = curr.next
    curr.next = None
    tail.next = head
    return new_head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = rotate_right(head, 2)
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
