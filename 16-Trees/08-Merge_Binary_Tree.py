# Megrge two binary trees

# Write a function that takes in two binary trees and merges them. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the non-null node will be used as the node of the new tree.

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 is None:
        return tree2
    elif tree2 is None:
        return tree1
        
    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1

