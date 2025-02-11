# Remove the duplicate elements from the linked list

# Time: O(n)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next


        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode 

    return linkedList

# Test the function

# Create a linked list

# 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

# Expected Output : 1 -> 3 -> 4 -> 5 -> 6


linkedList = LinkedList(1)
linkedList.next = LinkedList(1)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next = LinkedList(4)

linkedList.next.next.next.next.next.next = LinkedList(5)

linkedList.next.next.next.next.next.next.next = LinkedList(6)

removeDuplicatesFromLinkedList(linkedList)

print(linkedList.value) # 1
