class Solution:
    def maxOfMins(self, arr):
       # code here
        PSE = [-1]*len(arr)
        NSE = [len(arr)]*len(arr)
       
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                PSE[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                NSE[i] = stack[-1]
            stack.append(i)
        
        res = [0]*len(arr)
        for i in range(len(arr)):
            l = NSE[i]-PSE[i]-1
            res[l-1] = max(res[l-1],arr[i])
        
        for i in range(len(arr)-2,-1,-1):
            res[i] = max(res[i],res[i+1])
        
        return res