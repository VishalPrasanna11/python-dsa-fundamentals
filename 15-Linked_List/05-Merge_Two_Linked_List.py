# Merge Two Linked Lists    
# Merge two linked lists and return the intersection of the two linked lists.
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.

    listOneNodes = set()

    currentNodeOne = linkedListOne

    while currentNodeOne is not None:
        listOneNodes.add(currentNodeOne)
        currentNodeOne = currentNodeOne.next

    
    currentNodeTwo = linkedListTwo

    while currentNodeTwo is not None:
        if currentNodeTwo in listOneNodes:
            return currentNodeTwo
        currentNodeTwo= currentNodeTwo.next



    return None
