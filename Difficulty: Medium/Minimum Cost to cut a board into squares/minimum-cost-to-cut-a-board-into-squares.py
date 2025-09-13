import heapq
class Solution:
    def minCost(self, n, m, x, y):
        # code here
        cost = 0
        heap = []
        for el in x:
            heapq.heappush(heap,(-el,'x'))
        for el in y:
            heapq.heappush(heap,(-el,'y'))
        
        horizontalSegments,verticalSegments = 1,1
        while heap:
            c,seg = heapq.heappop(heap)
            if seg == 'x':
                cost+= c*horizontalSegments*-1
                verticalSegments+=1
            else:
                cost+= c*verticalSegments*-1
                horizontalSegments+=1
        return cost
        
        
        
