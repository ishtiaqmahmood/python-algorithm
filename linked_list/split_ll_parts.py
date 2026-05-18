class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def split_list_to_parts(head, k):
    """
    Splits a linked list into k consecutive parts.

    Args:
        head (ListNode): Head of list.
        k (int): Number of parts.

    Returns:
        list: List of ListNode heads.
    """
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    width, rem = divmod(length, k)
    res = []
    curr = head
    for i in range(k):
        head = curr
        for _ in range(width + (i < rem) - 1):
            if curr:
                curr = curr.next
        if curr:
            curr.next, curr = None, curr.next
        res.append(head)
    return res


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    parts = split_list_to_parts(head, 5)
    print(f"Split into {len(parts)} parts.")
