# For each element arr[i], let’s assume it is the maximum element in some subarray.
# We need to know:
# How far left and right can we extend while keeping arr[i] as the maximum?
# This gives us the maximum possible subarray length where arr[i] is the max.
class Solution:
    def longestSubarray(self, arr):
        n = len(arr)
        left = [-1]*n #leftmost as max
        right = [n]*n #rightmost as max
        
        #print(arr)
        
        #finding next greatest element!
        stack = []
        for i in range(len(arr)):
            if stack:
                while stack and arr[stack[-1]]<arr[i]:
                    right[stack.pop()]=i
            stack.append(i)
        
        #print(right)
        
        #finding next greates element backwards
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]<arr[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        #print(left)
        
        maxi = 0
        #keeping arr[i] as max
        for i in range(len(arr)):
            if arr[i]<=right[i]-left[i]-1:
                maxi = max(maxi,right[i]-left[i]-1)
        return maxi
            
        