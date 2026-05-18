class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node):
    """
    Deletes a node in a singly linked list (given access only to that node).

    Args:
        node (ListNode): Node to delete.
    """
    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    head = ListNode(4)
    node2 = ListNode(5)
    head.next = node2
    node2.next = ListNode(1)
    node2.next.next = ListNode(9)
    delete_node(node2)
    # List should be 4 -> 1 -> 9
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
