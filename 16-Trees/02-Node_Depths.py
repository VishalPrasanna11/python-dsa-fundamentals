# Node Depths
# The distance between a node in a Binary Tree and the tree's root is called the node's depth.

# Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

# Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

# Sample Input


# tree = BinaryTree(1)
# tree.left = BinaryTree(2)
# tree.right = BinaryTree(3)
# tree.left.left = BinaryTree(4)
# tree.left.right = BinaryTree(5)
# tree.right.left = BinaryTree(6)
# tree.right.right = BinaryTree(7)
# tree.left.left.left = BinaryTree(8)
# tree.left.left.right = BinaryTree(9)

# Sample Output

# 16

def nodeDepths(root):
    # Write your code here.
    sumofDepths = 0
    stack = [{"node":root,"depth":0}]

    while len(stack)>0:
        nodeInfo = stack.pop()
        node,depth = nodeInfo["node"],nodeInfo["depth"]
        if node is None:
            continue
        sumofDepths+=depth
        stack.append({"node":node.left,"depth":depth+1})
        stack.append({"node":node.right,"depth":depth+1})

    return sumofDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)
tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)


# Test the function

print(nodeDepths(tree)) # 16


# Time Complexity : O(n)
# Space Complexity : O(h) where h is the height of the tree

