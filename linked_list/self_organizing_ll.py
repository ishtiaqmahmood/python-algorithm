class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SelfOrganizingList:
    """
    Self-organizing list using Move-To-Front (MTF) strategy.
    """
    def __init__(self):
        self.head = None

    def search(self, val):
        if not self.head:
            return False
        if self.head.val == val:
            return True

        curr = self.head
        while curr.next:
            if curr.next.val == val:
                # MTF
                target = curr.next
                curr.next = target.next
                target.next = self.head
                self.head = target
                return True
            curr = curr.next
        return False

    def insert(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node


if __name__ == "__main__":
    sol = SelfOrganizingList()
    sol.insert(3)
    sol.insert(2)
    sol.insert(1)
    print(f"Search 3: {sol.search(3)}") # 3 will move to front
    print(f"Head value: {sol.head.val}")
