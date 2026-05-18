import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos: return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.pos: return False
        idx = self.pos[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        del self.pos[val]
        return True

    def get_random(self):
        return random.choice(self.nums)


if __name__ == "__main__":
    rs = RandomizedSet()
    rs.insert(1); rs.insert(2)
    print(f"Random: {rs.get_random()}")
