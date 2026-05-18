class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return True
            curr = curr.next
        return False


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.delete(2)
    curr = dll.head
    while curr:
        print(curr.val, end=" <-> ")
        curr = curr.next
    print("None")
