import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))
    #

    while (p.qsize() > 1):
        # greedily remove the two nodes x and y with lowest frequency,
        x = p.get()
        y = p.get()

        # create a new node z with x and y as children,
        z_freq = x.data[0] + y.data[0]
        z = TreeNode(x, y, (z_freq, ""))
        
        # insert z into the priority queue (using an empty character "")
        p.put(z)
    #

    # return root of the tree
    return p.get()
# make_huffman_tree

# TODO: perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    # perform a tree traversal and collect encodings for leaves in code
    
    # print(f"node data: {node.data}; prefix: {prefix}; code: {code}\n")
    # base case >>> leaf
    if node.children() == None:
        letter = node.data[1]
        code[letter] = prefix
        return code
    # otherwise >>> iterate through left and right
    else:
        left_code = get_code(node.left, prefix+'0', code)
        right_code = get_code(node.right, prefix+'1', code)

        # combine
        return {**left_code, **right_code}
    #
# get_code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    letter_cnt = len(f)
    total_cost = 0
    for letter, freq in f.items():
        # QUESTION: should this get rounded up to a base 2 number?
        encoding_cost = math.log(letter_cnt, 2)     # num bits to represent letter

        # letter cost = freq of letter + cost of encoding
        total_cost += freq * encoding_cost
    #

    return total_cost
# fixed_length_cost

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    total_cost = 0
    for letter, freq in f.items():
        encoding_cost = len(C[letter])

        # letter cost = freq of letter + cost of encoding
        total_cost += freq * encoding_cost
    #

    return total_cost
# huffman_cost

f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))

print(f)
print(sorted(C.items(), key=lambda item: len(item[1])))
