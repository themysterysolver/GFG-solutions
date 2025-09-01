# Bruting here with finiding maxima each time using sliding window with increment and decrement
# is O(N^2) 

#we will use SLIDING WINDOW+freq+stale logic+heap
#that is we pop el of heap if the count doens't match the frequency of the 
#current el's count

class Solution:
    def sumOfModes(self, arr, k):
        
        hash = defaultdict(int)
        for i in range(k):
            hash[arr[i]]+=1
        
        heap = []
        sumx = 0
        for key,count in hash.items():
            heapq.heappush(heap,(-count,key))
        def getMode():
            while heap:
                count,el = heap[0]
                if -count == hash[el]:
                    return el
                else:
                    heapq.heappop(heap)
            return 0
        
        sumx+=getMode()
        
        for i in range(k,len(arr)):
            # start = arr[i-k]
            hash[arr[i]]+=1
            heapq.heappush(heap,(-hash[arr[i]],arr[i]))
            hash[arr[i-k]]-=1
            heapq.heappush(heap,(-hash[arr[i-k]],arr[i-k]))
            sumx+=getMode()
        return sumx
            
                
                
            