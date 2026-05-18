class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head):
    """
    Sorts a linked list in O(n log n) time and O(1) space (excluding recursion stack).

    Args:
        head (ListNode): Head of linked list.

    Returns:
        ListNode: Sorted list head.
    """
    if not head or not head.next:
        return head

    # Split
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)

    # Merge
    dummy = ListNode()
    curr = dummy
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    curr.next = left or right
    return dummy.next


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sorted_head = sort_list(head)
    while sorted_head:
        print(sorted_head.val, end=" -> ")
        sorted_head = sorted_head.next
    print("None")
