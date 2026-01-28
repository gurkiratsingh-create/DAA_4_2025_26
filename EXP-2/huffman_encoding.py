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


def generate_codes(node, code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
        return
    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)


def decode(encoded, root):
    result = ""
    current = root
    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            result += current.char
            current = root
    return result


text = input("Enter a string: ")

freq = Counter(text)
heap = []

for ch, f in freq.items():
    heapq.heappush(heap, Node(ch, f))

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    node = Node(None, left.freq + right.freq)
    node.left = left
    node.right = right
    heapq.heappush(heap, node)

root = heap[0]

codes = {}
generate_codes(root, "", codes)

encoded = ""
for ch in text:
    encoded += codes[ch]

decoded = decode(encoded, root)

print("Original String:", text)
print("Encoded String:", encoded)
print("Decoded String:", decoded)
