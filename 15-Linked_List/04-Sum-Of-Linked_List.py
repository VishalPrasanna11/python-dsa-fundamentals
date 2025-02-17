# Sum of Linked List 

# Write a function that takes in the head of a Singly Linked List and returns the sum of all its elements.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

# You can assume that the input Linked List will always have at least one node.


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    newLinkedListHeadPonter = LinkedList(0)

    currentNode = newLinkedListHeadPonter
    carry = 0


    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry!=0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo+carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode= newNode

        carry = sumOfValues//10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None


    return newLinkedListHeadPonter.next
        
