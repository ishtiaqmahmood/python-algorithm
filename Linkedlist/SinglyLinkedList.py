class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    """
    A class to represent a singly linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_sll(self, value, location):
        """
        Inserts a node into the singly linked list at a given location.

        Args:
            value: The value to be inserted.
            location (int): The location where the value should be inserted.
                            0 for the beginning, 1 for the end, otherwise at the given index.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    if temp_node.next is None:
                        break
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if new_node.next is None:
                    self.tail = new_node


if __name__ == "__main__":
    singly_linked_list = SLinkedList()
    singly_linked_list.insert_sll(1, 1)
    singly_linked_list.insert_sll(2, 1)
    singly_linked_list.insert_sll(3, 1)
    singly_linked_list.insert_sll(4, 1)

    singly_linked_list.insert_sll(5, 0)
    singly_linked_list.insert_sll(9, 3)
    print([node.value for node in singly_linked_list])
