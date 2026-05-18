class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    """
    Deletes duplicates from a sorted linked list.

    Args:
        head (ListNode): Head of list.

    Returns:
        ListNode: Modified list head.
    """
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr.next = curr.next
            curr = curr.next
    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(1, ListNode(2)))
    res = delete_duplicates(head)
    while res:
        print(res.val, end=" -> ")
        res = res.next
    print("None")
