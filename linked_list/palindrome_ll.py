class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    """
    Checks if a linked list is a palindrome.

    Args:
        head (ListNode): Head of list.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals == vals[::-1]


if __name__ == "__main__":
    for vals in [[1, 2, 2, 1], [1, 2]]:
        head = None
        for v in reversed(vals):
            head = ListNode(v, head)
        print(f"Is {vals} palindrome? {is_palindrome(head)}")
