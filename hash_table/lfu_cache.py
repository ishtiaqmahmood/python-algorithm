from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.vals = {}
        self.freqs = {}
        self.lists = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key):
        if key not in self.vals: return -1
        val = self.vals[key]
        freq = self.freqs[key]
        del self.lists[freq][key]
        if not self.lists[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.freqs[key] += 1
        self.lists[freq + 1][key] = val
        return val

    def put(self, key, value):
        if self.capacity <= 0: return
        if key in self.vals:
            self.vals[key] = value
            self.get(key)
            return
        if len(self.vals) >= self.capacity:
            k, _ = self.lists[self.min_freq].popitem(last=False)
            del self.vals[k]; del self.freqs[k]
        self.vals[key] = value
        self.freqs[key] = 1
        self.lists[1][key] = value
        self.min_freq = 1


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1); lfu.put(2, 2)
    print(f"get(1): {lfu.get(1)}")
    lfu.put(3, 3)
    print(f"get(2): {lfu.get(2)}")
