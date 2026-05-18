class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head):
    """
    Flattens a multilevel doubly linked list.

    Args:
        head (Node): Head of the list.

    Returns:
        Node: Head of the flattened list.
    """
    if not head:
        return head

    dummy = Node(0, None, head, None)
    stack = [head]
    prev = dummy

    while stack:
        curr = stack.pop()
        prev.next = curr
        curr.prev = prev

        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr

    dummy.next.prev = None
    return dummy.next


if __name__ == "__main__":
    # Simplified test
    head = Node(1)
    head.child = Node(2)
    flattened = flatten(head)
    print("Flattened list values: ", end="")
    while flattened:
        print(flattened.val, end=" -> ")
        flattened = flattened.next
    print("None")
