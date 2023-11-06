class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

def print_nodes(node, val=""):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

chars = []
freq = []
num_chars = int(input("Enter the number of characters: "))

for i in range(num_chars):
    char = input(f"Enter character {i + 1}: ")
    frequency = int(input(f"Enter frequency for character {char}: "))
    chars.append(char)
    freq.append(frequency)

nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    left.huff = 0
    right.huff = 1
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print("Characters:", chars)
print("Frequency:", freq, "\nHuffman Encoding:")
print_nodes(nodes[0])






# Certainly! This Python code implements Huffman coding, a greedy algorithm used for lossless data compression. Huffman coding works by assigning variable-length codes to input characters based on their frequencies, with more frequent characters getting shorter codes. Let me break down the code step by step:

# 1. **Class Definition - Node**:
#    ```python
#    class Node:
#        def __init__(self, freq, symbol, left=None, right=None):
#            self.freq = freq
#            self.symbol = symbol
#            self.left = left
#            self.right = right
#            self.huff = ""
#    ```
#    This defines a class called `Node` representing a node in the Huffman tree. Each node has a frequency (`freq`), a symbol (`symbol`), and pointers to its left and right children. The `huff` attribute stores the Huffman code for the character represented by the node.

# 2. **`print_nodes` Function**:
#    ```python
#    def print_nodes(node, val=""):
#        new_val = val + str(node.huff)
#        if node.left:
#            print_nodes(node.left, new_val)
#        if node.right:
#            print_nodes(node.right, new_val)
#        if not node.left and not node.right:
#            print(f"{node.symbol} -> {new_val}")
#    ```
#    This function recursively traverses the Huffman tree and prints the characters along with their Huffman codes.

# 3. **Input Processing**:
#    ```python
#    chars = []
#    freq = []
#    num_chars = int(input("Enter the number of characters: "))
#    for i in range(num_chars):
#        char = input(f"Enter character {i + 1}: ")
#        frequency = int(input(f"Enter frequency for character {char}: "))
#        chars.append(char)
#        freq.append(frequency)
#    ```
#    This section takes user input for the characters and their corresponding frequencies.

# 4. **Node Initialization**:
#    ```python
#    nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]
#    ```
#    Nodes are created for each character with its frequency and added to the `nodes` list.

# 5. **Huffman Tree Construction**:
#    ```python
#    while len(nodes) > 1:
#        nodes = sorted(nodes, key=lambda x: x.freq)
#        left = nodes[0]
#        right = nodes[1]
#        left.huff = 0
#        right.huff = 1
#        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
#        nodes.remove(left)
#        nodes.remove(right)
#        nodes.append(newNode)
#    ```
#    This loop constructs the Huffman tree by repeatedly merging the two nodes with the lowest frequencies, assigning Huffman codes `0` and `1` to their left and right children respectively, and creating a new node with the combined frequency.

# 6. **Printing Huffman Codes**:
#    ```python
#    print("Characters:", chars)
#    print("Frequency:", freq, "\nHuffman Encoding:")
#    print_nodes(nodes[0])
#    ```
#    Finally, the code prints the input characters, their frequencies, and their corresponding Huffman codes using the `print_nodes` function.

# This program demonstrates the Huffman coding algorithm by constructing a Huffman tree based on the user-provided characters and frequencies, and then printing the Huffman codes for each character.

# Let's analyze the time and space complexity of the given Huffman coding implementation:

# ### Time Complexity:
# 1. **Input Processing:**
#    - Reading characters and frequencies: O(N), where N is the number of characters.

# 2. **Node Initialization:**
#    - Creating nodes for characters: O(N), where N is the number of characters.

# 3. **Huffman Tree Construction:**
#    - Sorting nodes: O(N log N), where N is the number of nodes (characters).
#    - Constructing the Huffman tree: O(N log N), where N is the number of nodes (characters). In the worst case, the loop iterates N-1 times, each time sorting the nodes list.

# 4. **Printing Huffman Codes:**
#    - Printing the Huffman codes: O(N), where N is the number of characters. In the worst case, the function visits each leaf node once.

# Therefore, the overall time complexity of the given code is O(N log N) due to the sorting step in Huffman tree construction.

# ### Space Complexity:
# 1. **Input Characters and Frequencies:**
#    - Storage for input characters and frequencies: O(N), where N is the number of characters.

# 2. **Nodes List:**
#    - Storage for nodes: O(N), where N is the number of characters.

# 3. **Huffman Tree:**
#    - Space used by the Huffman tree: O(N), where N is the number of nodes (characters).

# 4. **Recursive Call Stack:**
#    - During the recursive traversal of the Huffman tree, the maximum depth of the recursion is N (number of characters). Therefore, the space used by the call stack is O(N).

# Therefore, the overall space complexity of the given code is O(N).