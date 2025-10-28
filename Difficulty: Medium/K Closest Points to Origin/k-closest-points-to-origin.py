
import heapq,math
class Solution:
    def kClosest(self, points, k):
        # code here
        
        def distance(x1,y1,x2,y2):
            return math.sqrt((x2-x1)**2+(y2-y1)**2)
        heap = []
        for x,y in points:
            heapq.heappush(heap,(distance(x,y,0,0),[x,y]))
        result = []
        for i in range(k):
            _,el = heapq.heappop(heap)
            result.append(el)
        return result