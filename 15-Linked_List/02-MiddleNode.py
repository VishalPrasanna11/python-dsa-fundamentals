# Return the Middel Node of a Linked List

# Time: O(n) - To traverse the list


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    currentNode = linkedList
    count = 0
    while currentNode  is not None:
        count+=1
        currentNode=currentNode.next

    middleNode = linkedList
    for _ in range(count//2):
        middleNode = middleNode.next
    return middleNode



# Test the function

# Create a linked list

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

# Expected Output : 5

linkedList = LinkedList(1)
linkedList.next = LinkedList(2)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(5)
linkedList.next.next.next.next.next = LinkedList(6)


middleNode = middleNode(linkedList)

print(middleNode.value) # 5