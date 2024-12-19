# Queues
# A queue is a collection of objects that are inserted and removed according to the first-in, first-out (FIFO) principle.
# The queue data structure is similar to the stack. The difference between a stack and a queue is that in a stack, the last element added is the first element that can be removed. In a queue, the first element added is the first element that can be removed.

# Queue Operations
# The main operations that can be performed on a queue are:
# Enqueue: Adds an element to the end of the queue.
# Dequeue: Removes an element from the front of the queue.
# Peek or Front: Returns the element at the front of the queue.
# isEmpty: Checks if the queue is empty.
# isFull: Checks if the queue is full.

# Queue Implementation

# Queue implementation using list

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == 10

    def __str__(self):
        return str(self.queue)
    
# Test the queue implementation
queue = Queue()
print(queue)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.dequeue())
print(queue)
print(queue.peek())

# Time Complexity of Queue Operations:
# Enqueue: O(1)
# Dequeue: O(n)
# Peek: O(1)
# isEmpty: O(1)


