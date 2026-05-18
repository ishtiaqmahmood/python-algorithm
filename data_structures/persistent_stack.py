class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class PersistentStack:
    def push(self, head, val):
        return Node(val, head)

    def pop(self, head):
        if not head: return None
        return head.next


if __name__ == "__main__":
    ps = PersistentStack()
    v1 = ps.push(None, 1)
    v2 = ps.push(v1, 2)
    print(f"V1: {v1.val}, V2: {v2.val}, V2-next: {v2.next.val}")
