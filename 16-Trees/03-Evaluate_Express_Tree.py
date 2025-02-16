# Evaluate an expression tree

# Given an expression tree, evaluate the expression and return the result.

# if -1 : Add the left and right child nodes
# if -2 : Subtract the left and right child nodes
# if -3 : Divide the left and right child nodes
# if -4 : Multiply the left and right child nodes

# The tree has nodes with values stored in a property called "value" and children stored in a property called "children". Children are an array of nodes.



# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.
    if tree.value >= 0:
        return tree.value

    leftvalue = evaluateExpressionTree(tree.left)
    rightvalue = evaluateExpressionTree(tree.right)

    if tree.value ==-1:
        return leftvalue+rightvalue
    elif tree.value == -2:
        return leftvalue-rightvalue
    elif tree.value == -3:
        return int(leftvalue//rightvalue)
    else : 
        return leftvalue*rightvalue
    
    
    
# Test the function

# Create a binary tree


tree = BinaryTree(-1)
tree.left = BinaryTree(-2)
tree.right = BinaryTree(-3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

print(evaluateExpressionTree(tree)) # 6

# Time Complexity: O(n)

# Space Complexity: O(n) - For the recursive call stack