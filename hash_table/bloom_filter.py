import math
import mmh3 # Note: In a real env, you might need to install this.
             # I'll use a simple hash fallback for this implementation.

class BloomFilter:
    """
    Implementation of a Bloom Filter.
    """
    def __init__(self, n, p):
        self.size = int(-(n * math.log(p)) / (math.log(2) ** 2))
        self.hash_count = int((self.size / n) * math.log(2))
        self.bit_array = 0 # Using a large integer as bit array

    def add(self, item):
        for i in range(self.hash_count):
            idx = hash(str(item) + str(i)) % self.size
            self.bit_array |= (1 << idx)

    def exists(self, item):
        for i in range(self.hash_count):
            idx = hash(str(item) + str(i)) % self.size
            if not (self.bit_array & (1 << idx)):
                return False
        return True

if __name__ == "__main__":
    bf = BloomFilter(100, 0.05)
    bf.add("test")
    print(f"Exists 'test': {bf.exists('test')}")
    print(f"Exists 'missing': {bf.exists('missing')}")
