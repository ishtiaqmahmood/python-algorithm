class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertion_sort_list(head):
    """
    Sorts a linked list using insertion sort.

    Args:
        head (ListNode): Head of list.

    Returns:
        ListNode: Sorted list head.
    """
    dummy = ListNode()
    curr = head
    while curr:
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        next_node = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next_node
    return dummy.next


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    res = insertion_sort_list(head)
    while res:
        print(res.val, end=" -> ")
        res = res.next
    print("None")
