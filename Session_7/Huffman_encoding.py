import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root, current_code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", huffman_codes)
    generate_codes(root.right, current_code + "1", huffman_codes)


def huffman_encoding(text):
    root = build_huffman_tree(text)
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]

    return encoded_text, huffman_codes


# Example Usage
text = "huffman encoding"
encoded_text, codes = huffman_encoding(text)

print("Original Text:", text)
print("Encoded Text:", encoded_text)
print("Huffman Codes:")
for char, code in codes.items():
    print(f"{char}: {code}")
