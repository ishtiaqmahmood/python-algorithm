class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head):
    """
    Copies a linked list with next and random pointers.

    Args:
        head (Node): Head of the list.

    Returns:
        Node: Head of the copied list.
    """
    if not head:
        return None

    # Step 1: Create new nodes and interweave them
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next

    # Step 2: Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the lists
    curr = head
    new_head = head.next
    while curr:
        temp = curr.next
        curr.next = temp.next
        if temp.next:
            temp.next = temp.next.next
        curr = curr.next
    return new_head


if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2; node2.next = node3; node3.next = node4; node4.next = node5
    node2.random = node1; node3.random = node5; node4.random = node3; node5.random = node1
    copied = copy_random_list(node1)
    print("List copied successfully.")
