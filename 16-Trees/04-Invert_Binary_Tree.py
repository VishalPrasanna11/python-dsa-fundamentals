# Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node.

def invertBinaryTree(tree):
    # Write your code here.
    queue = [tree]
    while len(queue):
        current= queue.pop()
        if current is None:
            continue
        swapLeftandRight(current)
        queue.append(current.left)
        queue.append(current.right)
    
def swapLeftandRight(tree):
    tree.left,tree.right = tree.right,tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Test the function

# Create a binary tree

binaryTree = BinaryTree(1)
binaryTree.left = BinaryTree(2)
binaryTree.right = BinaryTree(3)
binaryTree.left.left = BinaryTree(4)
binaryTree.left.right = BinaryTree(5)
binaryTree.right.left = BinaryTree(6)
binaryTree.right.right = BinaryTree(7)
binaryTree.left.left.left = BinaryTree(8)
binaryTree.left.left.right = BinaryTree(9)


invertBinaryTree(binaryTree)

# The tree should now be inverted

print(binaryTree.left.value) # 9
print(binaryTree.right.value) # 8

print(binaryTree.left.left.value) # 5
print(binaryTree.left.right.value) # 4

print(binaryTree.right.left.value) # 7

