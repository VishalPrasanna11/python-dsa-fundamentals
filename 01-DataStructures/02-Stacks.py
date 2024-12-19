# Stack implemetion in Python

# Stack is a linear data structure which follows a particular order in which the operations are performed.
# The order may be LIFO(Last In First Out) or FILO(First In Last Out).

# Mainly the following three basic operations are performed in the stack:

# Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
# Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.

# Peek or Top: Returns top element of stack.


# Stack implementation using list

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)
    
# Test the stack implementation
stack = Stack()
print(stack)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())

# Time Complexity of Stack Operations:
# Push: O(1)
# Pop: O(1)

# Space Complexity of Stack Operations:
# Push: O(1)
# Pop: O(1)
