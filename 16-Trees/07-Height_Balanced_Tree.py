# Height Balanced Tree
# Write a function that takes in a Binary Tree and returns a boolean representing whether the Binary Tree is height balanced.
# A Binary Tree is said to be height balanced if for each node in the tree, the difference between the height of its left subtree and the height of its right subtree is at most 1.
# Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,isBalanced,height):
        self.isBalanced = isBalanced
        self.height = height


    
def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):

    if node == None:
        return TreeInfo(True,-1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)


    isBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    height = max(leftSubTreeInfo.height,rightSubTreeInfo.height)+1

    return TreeInfo(isBalanced,height)


    
