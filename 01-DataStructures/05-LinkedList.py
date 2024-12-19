# Linked List
# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# The elements in a linked list are linked using pointers. Each element in the linked list is called a node.

# Types of Linked List
# There are three types of linked lists:
# Singly Linked List: Each node in a singly linked list points to the next node in the sequence.
# Doubly Linked List: Each node in a doubly linked list points to the next node and the previous node in the sequence.
# Circular Linked List: In a circular linked list, the last node points back to the first node.

# Linked List Operations
# The main operations that can be performed on a linked list are:
# Insert: Adds an element to the linked list.
# Delete: Removes an element from the linked list.
# Search: Searches for an element in the linked list.
# Traverse: Visits each node in the linked list and performs a specific operation.

# Linked List Implementation

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Linked List class

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None
        
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Test the linked list implementation
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.traverse()
linked_list.delete(2)
linked_list.traverse()
print(linked_list.search(3))

# Time Complexity of Linked List Operations:
# Insert: O(1) - O(n)
# Delete: O(1) - O(n)
# Search: O(n)
# Traverse: O(n)

# Doubly Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        
    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                else:
                    nxt = current_node.next
                    current_node.next = None
                    nxt.prev = None
                    current_node = None
                    self.head = nxt
                    return
            elif current_node.data == data:
                if current_node.next:
                    nxt = current_node.next
                    prev = current_node.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next
            
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Test the doubly linked list implementation
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert(1)
doubly_linked_list.insert(2)
doubly_linked_list.insert(3)
doubly_linked_list.traverse()

doubly_linked_list.delete(2)
doubly_linked_list.traverse()

print(doubly_linked_list.search(3))

# Time Complexity of Doubly Linked List Operations:

# Insert: O(1)
# Delete: O(1) - O(n)
# Search: O(n)
# Traverse: O(n)

# Circular Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Circular Linked List class

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
        self.head = new_node
    
    def delete(self, data):
        current_node = self.head
        prev = None
        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    temp = current_node
                    while temp.next != self.head:
                        temp = temp.next
                    if self.head == self.head.next:
                        self.head = None
                    else:
                        temp.next = self.head.next
                        self.head = self.head.next
                    current_node = None
                    return
                else:
                    prev.next = current_node.next
                    current_node = None
                    return
            elif current_node.next == self.head:
                break
            prev = current_node
            current_node = current_node.next
        
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
            if current_node == self.head:
                return False
        return False
    
    def traverse(self):
        current_node = self.head
        if current_node:
            while True:
                print(current_node.data)
                current_node = current_node.next
                if current_node == self.head:
                    break

# Test the circular linked list implementation
circular_linked_list = CircularLinkedList()
circular_linked_list.insert(1)
circular_linked_list.insert(2)
circular_linked_list.insert(3)
circular_linked_list.traverse()
circular_linked_list.delete(2)

circular_linked_list.traverse()
print(circular_linked_list.search(3))

# Time Complexity of Circular Linked List Operations:

# Insert: O(1)
# Delete: O(n)
# Search: O(n)

