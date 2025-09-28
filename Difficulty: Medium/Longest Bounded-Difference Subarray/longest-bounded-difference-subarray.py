class Solution:
    def longestSubarray(self, arr, x):
        #code here
        minQ = deque([])
        maxQ = deque([])
        n  = len(arr)
        start = end = resStart = resEnd = 0
        
        while end<n:
            
            while minQ and arr[minQ[-1]]>arr[end]:
                minQ.pop()
            
            while maxQ and arr[maxQ[-1]]<arr[end]:
                maxQ.pop()
            
            minQ.append(end)
            maxQ.append(end)
            
            while arr[maxQ[0]]-arr[minQ[0]]>x:
                if start == minQ[0]:
                    minQ.popleft()
                if start == maxQ[0]:
                    maxQ.popleft()
                start+=1
            
            if end-start >resEnd-resStart:
                resStart,resEnd = start,end
            
            end+=1
        
        return arr[resStart:resEnd+1]