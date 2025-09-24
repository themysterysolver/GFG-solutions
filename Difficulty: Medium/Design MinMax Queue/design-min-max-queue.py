import heapq
from collections import deque

class SpecialQueue:
    def __init__(self):
        # Define Data Structures
        self.q = deque([])
        self.minq = deque([])
        self.maxq = deque([])
    def enqueue(self, x):
        # Insert element into the queue
        self.q.append(x)
        while self.minq and self.minq[-1]>x:
            self.minq.pop()
        self.minq.append(x)
        
        while self.maxq and self.maxq[-1]<x:
            self.maxq.pop()
        self.maxq.append(x)
    
    def dequeue(self):
        # Remove element from the queue
        el = self.q.popleft()
        if self.minq and el == self.minq[0]:
            self.minq.popleft()
        if self.maxq and el == self.maxq[0]:
            self.maxq.popleft()
        return el
        
    
    def getFront(self):
        # Get front element
        return self.q[0]
    
    def getMin(self):
        # Get minimum element
        return self.minq[0]
    
    def getMax(self):
        # Get maximum element
        return self.maxq[0]