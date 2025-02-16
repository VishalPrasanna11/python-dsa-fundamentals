# Difficulty: Medium
# Symmetrical Trees
# Write a function that takes in a Binary Tree and returns a boolean representing whether the Binary Tree is symmetrical.
# A Binary Tree is said to be symmetrical if it is the same as its mirror image.
# Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    # Write your code here.
    return symetricalTreeHelper(tree.left,tree.right)

def symetricalTreeHelper(left,right):
    if right is not None and left is not None:
        if left.value == right.value:
            return symetricalTreeHelper(left.left,right.right) and symetricalTreeHelper(left.right,right.left)

    return left == right