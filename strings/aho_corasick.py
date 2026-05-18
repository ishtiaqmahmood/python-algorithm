from collections import deque


class AhoCorasick:
    """
    Aho-Corasick algorithm for multi-pattern matching.
    """
    def __init__(self, patterns):
        self.trie = [{}]
        self.fail = [0]
        self.output = [[]]
        for pattern in patterns:
            self._insert(pattern)
        self._build()

    def _insert(self, pattern):
        node = 0
        for char in pattern:
            if char not in self.trie[node]:
                self.trie[node][char] = len(self.trie)
                self.trie.append({})
                self.fail.append(0)
                self.output.append([])
            node = self.trie[node][char]
        self.output[node].append(pattern)

    def _build(self):
        queue = deque()
        for char, next_node in self.trie[0].items():
            queue.append(next_node)
        while queue:
            u = queue.popleft()
            for char, v in self.trie[u].items():
                f = self.fail[u]
                while char not in self.trie[f] and f != 0:
                    f = self.fail[f]
                self.fail[v] = self.trie[f].get(char, 0)
                self.output[v].extend(self.output[self.fail[v]])
                queue.append(v)

    def search(self, text):
        node = 0
        results = []
        for i, char in enumerate(text):
            while char not in self.trie[node] and node != 0:
                node = self.fail[node]
            node = self.trie[node].get(char, 0)
            for pattern in self.output[node]:
                results.append((i - len(pattern) + 1, pattern))
        return results


if __name__ == "__main__":
    patterns = ["he", "she", "his", "hers"]
    text = "ushers"
    ac = AhoCorasick(patterns)
    print(f"Patterns found in '{text}': {ac.search(text)}")
