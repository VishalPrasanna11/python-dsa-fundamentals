# Binary Tree Diameter

# Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree.


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height+rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter,rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot,maxDiameterSoFar)
    currentHeight = 1+max(leftTreeInfo.height,rightTreeInfo.height)

    return TreeInfo(currentDiameter,currentHeight)
class TreeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height
        
        
        
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

print(binaryTreeDiameter(binaryTree))
