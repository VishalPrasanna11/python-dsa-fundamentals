# Branch Sum 

# Find the sum of all the branches in a binary tree. A branch is a path from the root node to a leaf node.

# The tree has nodes with values stored in a property called "value" and children stored in a property called "children". Children are an array of nodes.

# The tree is a binary tree if it has at most 2 children, left and right.


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    branchSumHelper(root, 0, sums)
    return sums

def branchSumHelper(node, runningSum, sums):
    if node is None:
        return
    
    newRunningSum = runningSum  + node.value
    if node.left is None and node.right is None :
        sums.append(newRunningSum)
        return

    branchSumHelper(node.left, newRunningSum, sums)
    branchSumHelper(node.right, newRunningSum, sums)
    
    
    
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
binaryTree.left.right.left = BinaryTree(10)


print(branchSums(binaryTree)) # [15, 16, 18, 10, 11]
