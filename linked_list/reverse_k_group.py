class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    """
    Reverses nodes of a linked list k at a time.

    Args:
        head (ListNode): Head of list.
        k (int): Group size.

    Returns:
        ListNode: Head of modified list.
    """
    curr = head
    count = 0
    while curr and count != k:
        curr = curr.next
        count += 1

    if count == k:
        curr = reverse_k_group(curr, k)
        while count > 0:
            tmp = head.next
            head.next = curr
            curr = head
            head = tmp
            count -= 1
        head = curr
    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = reverse_k_group(head, 2)
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
