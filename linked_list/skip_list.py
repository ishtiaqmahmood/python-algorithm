import random


class SkipListNode:
    def __init__(self, val=None, levels=1):
        self.val = val
        self.next = [None] * levels


class SkipList:
    """
    Skip List implementation.
    """
    def __init__(self, max_levels=16):
        self.max_levels = max_levels
        self.head = SkipListNode(levels=max_levels)
        self.level_count = 1

    def search(self, val):
        curr = self.head
        for i in range(self.level_count - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < val:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr is not None and curr.val == val

    def insert(self, val):
        level = 1
        while level < self.max_levels and random.random() < 0.5:
            level += 1

        if level > self.level_count:
            self.level_count = level

        new_node = SkipListNode(val, level)
        curr = self.head
        for i in range(self.level_count - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < val:
                curr = curr.next[i]
            if i < level:
                new_node.next[i] = curr.next[i]
                curr.next[i] = new_node


if __name__ == "__main__":
    sl = SkipList()
    sl.insert(3)
    sl.insert(1)
    sl.insert(2)
    print(f"Search 2: {sl.search(2)}")
    print(f"Search 4: {sl.search(4)}")
