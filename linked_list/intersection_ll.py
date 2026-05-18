class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(head_a, head_b):
    """
    Finds the node at which the intersection of two singly linked lists begins.

    Args:
        head_a (ListNode): Head of first list.
        head_b (ListNode): Head of second list.

    Returns:
        ListNode: Intersection node or None.
    """
    if not head_a or not head_b:
        return None
    a, b = head_a, head_b
    while a != b:
        a = a.next if a else head_b
        b = b.next if b else head_a
    return a


if __name__ == "__main__":
    common = ListNode(8, ListNode(4, ListNode(5)))
    head1 = ListNode(4, ListNode(1, common))
    head2 = ListNode(5, ListNode(6, ListNode(1, common)))
    intersect = get_intersection_node(head1, head2)
    print(f"Intersection at node with value: {intersect.val if intersect else None}")
