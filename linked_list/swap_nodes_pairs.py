class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    """
    Swaps every two adjacent nodes in a linked list.

    Args:
        head (ListNode): Head of list.

    Returns:
        ListNode: Head of swapped list.
    """
    if not head or not head.next:
        return head

    first = head
    second = head.next

    first.next = swap_pairs(second.next)
    second.next = first

    return second


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    swapped = swap_pairs(head)
    while swapped:
        print(swapped.val, end=" -> ")
        swapped = swapped.next
    print("None")
