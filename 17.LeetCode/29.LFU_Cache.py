class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, capacity: int):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev.next = node  # Fixed this line
        self.right.prev = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev 
            prev.next = next
            self.map.pop(val, None)
    
    def popLeft(self):
        if self.left.next == self.right:
            return -1  # Empty list
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRight(val)


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0  # Minimum frequency
        self.valMap = {}  # key -> value
        self.countMap = {}  # key -> frequency
        self.listMap = {}  # frequency -> LinkedList of keys with that frequency
        
        # Initialize with empty LinkedLists
        for i in range(200):  # assuming max frequency won't exceed 200
            self.listMap[i] = LinkedList(capacity)
    
    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)
        
        # If no keys with the current minimum frequency, update lfuCnt
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        
        # Update frequency
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
            
        # If key exists, update value and frequency
        if key in self.valMap:
            self.valMap[key] = value
            self.counter(key)
            return
        
        # If cache is full, remove least frequently used item
        if len(self.valMap) >= self.cap:
            # Get the key from the LFU list
            lfu_key = self.listMap[self.lfuCnt].popLeft()
            if lfu_key != -1:
                self.valMap.pop(lfu_key, None)
                self.countMap.pop(lfu_key, None)
        
        # Add new item with frequency 1
        self.valMap[key] = value
        self.countMap[key] = 1
        self.listMap[1].pushRight(key)
        self.lfuCnt = 1  # Reset min frequency to 1