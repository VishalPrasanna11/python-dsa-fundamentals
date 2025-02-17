# Reeverse Linekd List

# The famous reverse linked list problem. Given the head of a singly linked list, reverse the list, and return the reversed list's head.


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    previousNode, currentNode  = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

    return previousNode
