class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates_ii(head):
    """
    Deletes all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

    Args:
        head (ListNode): Head of list.

    Returns:
        ListNode: Modified list head.
    """
    dummy = ListNode(0, head)
    prev = dummy
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    res = delete_duplicates_ii(head)
    while res:
        print(res.val, end=" -> ")
        res = res.next
    print("None")
