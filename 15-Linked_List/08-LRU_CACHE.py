# LRU Cache
# Difficulty: Hard
# Implement an LRU (Least Recently Used) cache. An LRU cache is a cache data structure that has limited space, and once there are more items in the cache than available space, it will preempt the least recently used item. This algorithm is used to optimize the use of a cache - if the cache is full and we want to add a new item, we evict the item that hasn't been used in the longest amount of time.


class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1  # Fixed syntax error: += instead of + =
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)  # Fixed method name typo
        self.updateMostRecent(self.cache[key])  # Fixed method name typo
           
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])  # Fixed method name
        return self.cache[key].value
      
    def getMostRecentKey(self):
        if self.listOfMostRecent.head is None:
            return None
        return self.listOfMostRecent.head.key

    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]  # Added missing cache cleanup

    def replaceKey(self, key, value):  # Fixed method name typo
        if key not in self.cache:
            raise Exception("The provided key isn't in cache!")
        self.cache[key].value = value

    def updateMostRecent(self, node):  # Fixed method name typo
        self.listOfMostRecent.setHeadTo(node)

class DoublyLinkedList:  # Fixed class name typo
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:  # Fixed variable name typo
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail  # Fixed variable name typo
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None