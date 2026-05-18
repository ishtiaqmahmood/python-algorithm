class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head):
    """
    Groups all odd nodes together followed by the even nodes.

    Args:
        head (ListNode): Head of list.

    Returns:
        ListNode: Modified list head.
    """
    if not head:
        return None
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = odd_even_list(head)
    while res:
        print(res.val, end=" -> ")
        res = res.next
    print("None")
