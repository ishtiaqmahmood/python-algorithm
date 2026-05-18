class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers_ii(l1, l2):
    """
    Adds two numbers represented by linked lists (most significant digit first).

    Args:
        l1 (ListNode): First list.
        l2 (ListNode): Second list.

    Returns:
        ListNode: Result list.
    """
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next

    head = None
    carry = 0
    while s1 or s2 or carry:
        v1 = s1.pop() if s1 else 0
        v2 = s2.pop() if s2 else 0
        val = v1 + v2 + carry
        carry = val // 10
        new_node = ListNode(val % 10)
        new_node.next = head
        head = new_node
    return head


if __name__ == "__main__":
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = add_two_numbers_ii(l1, l2)
    while res:
        print(res.val, end=" -> ")
        res = res.next
    print("None")
