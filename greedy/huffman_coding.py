import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(chars, freq):
    """
    Generates Huffman Codes for a given set of characters and frequencies.

    Args:
        chars (list): Characters.
        freq (list): Frequencies.

    Returns:
        dict: Character to Huffman code mapping.
    """
    heap = [Node(chars[i], freq[i]) for i in range(len(chars))]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes


if __name__ == "__main__":
    c = ['a', 'b', 'c', 'd', 'e', 'f']
    f = [5, 9, 12, 13, 16, 45]
    print(f"Huffman Codes: {huffman_coding(c, f)}")
