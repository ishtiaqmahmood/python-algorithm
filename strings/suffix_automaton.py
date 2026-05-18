class SuffixAutomatonNode:
    def __init__(self, length=0, link=-1):
        self.len = length
        self.link = link
        self.next = {}


class SuffixAutomaton:
    """
    Suffix Automaton (SAM) for a string.
    """
    def __init__(self, s):
        self.nodes = [SuffixAutomatonNode()]
        self.last = 0
        for char in s:
            self.extend(char)

    def extend(self, char):
        cur = len(self.nodes)
        self.nodes.append(SuffixAutomatonNode(self.nodes[self.last].len + 1))
        p = self.last
        while p != -1 and char not in self.nodes[p].next:
            self.nodes[p].next[char] = cur
            p = self.nodes[p].link
        if p == -1:
            self.nodes[cur].link = 0
        else:
            q = self.nodes[p].next[char]
            if self.nodes[p].len + 1 == self.nodes[q].len:
                self.nodes[cur].link = q
            else:
                clone = len(self.nodes)
                self.nodes.append(SuffixAutomatonNode(self.nodes[p].len + 1, self.nodes[q].link))
                self.nodes[clone].next = self.nodes[q].next.copy()
                while p != -1 and self.nodes[p].next.get(char) == q:
                    self.nodes[p].next[char] = clone
                    p = self.nodes[p].link
                self.nodes[q].link = self.nodes[cur].link = clone
        self.last = cur


if __name__ == "__main__":
    s = "abcbc"
    sam = SuffixAutomaton(s)
    print(f"SAM for '{s}' built with {len(sam.nodes)} nodes.")
