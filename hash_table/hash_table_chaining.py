class HashTableChaining:
    """
    Hash Table with Chaining for collision resolution.
    """
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

if __name__ == "__main__":
    ht = HashTableChaining()
    ht.put("apple", 10)
    ht.put("banana", 20)
    print(f"Value for 'banana': {ht.get('banana')}")
