#User function Template for python3
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        heap = []
        for a in arr:
            heapq.heappush(heap,a)
        #print(heap,'doajd')
        while heap and k!=1:
            heapq.heappop(heap)
            k-=1
        return heapq.heappop(heap) if heap else -1
        
