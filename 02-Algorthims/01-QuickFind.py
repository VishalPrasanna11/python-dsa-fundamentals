# Dyanmic Connnectivity Problem 

#Reflexive: p is connected to p
#Symmetric: if p is connected to q, then q is connected to p
#Transitive: if p is connected to q and q is connected to r, then p is connected to r
#Quick Find
#Data Structure: Integer array id[] of size N
#Find: Check if p and q have the same id
#Union: To merge components containing p and q, change all entries whose id equals id[p] to id[q]
#Complexity: O(N^2)
# Adding stopwatch to measure the time taken to run the code
class QuickFind:
         
    def __init__(self, N):
        self.id = [i for i in range(N)]
        
    def connected(self, p, q):
        return self.id[p] == self.id[q]
    
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
        print(self.id)
        


#Optimization: Quick Union

#Data Structure: Integer array id[] of size N
#Find: Check if p and q have the same root
#Union: To merge components containing p and q, set the id of p's root to the id of q's root

class QuickUnionOptimized:
    def __init__(self, N):
        self.id = [i for i in range(N)]
        
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j
        print(self.id)
    
#Optimization: Weighted Quick Union

#Data Structure: Integer array id[] of size N, Integer array sz[] of size N
#Find: Check if p and q have the same root
#Union: To merge components containing p and q, set the id of p's root to the id of q's root

class WeightedQuickUnion:
    def __init__(self, N):
        self.id = [i for i in range(N)]
        self.sz = [1 for i in range(N)]
        
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        print(self.id)
    

#measuring the time taken to run the code
import time

# Measure performance
def measure_performance(union_find_class, operations):
    print(f"Testing {union_find_class.__name__}...")
    start_time = time.time()  # Start stopwatch
    uf = union_find_class(10)
    for operation in operations:
        op, p, q = operation
        if op == "union":
            uf.union(p, q)
        elif op == "connected":
            print(f"Connected({p}, {q}): {uf.connected(p, q)}")
    elapsed_time = time.time() - start_time  # End stopwatch
    print(f"Time taken: {elapsed_time:.6f} seconds\n")

operations = [
    ("union", 4, 3),
    ("union", 3, 8),
    ("union", 6, 5),
    ("union", 9, 4),
    ("union", 2, 1),
    ("union", 8, 9),
    ("union", 5, 0),
    ("union", 7, 2),
    ("union", 6, 1),
    ("union", 1, 0),
    ("union", 6, 7),
    ("connected", 0, 7),
]

measure_performance(QuickFind, operations)
measure_performance(QuickUnionOptimized, operations)
measure_performance(WeightedQuickUnion, operations)
