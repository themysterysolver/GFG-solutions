class Solution:
    def maxLen(self, arr):
        # code here
        mp = {}
    
        preSum = 0
        res = 0
    
        # Traverse through the given array
        for i in range(len(arr)):
    
            # Add current element to sum
            # if current element is zero, add -1
            preSum += -1 if arr[i] == 0 else 1
    
            # To handle sum = 0 at last index
            if preSum == 0:
                res = i + 1
    
            # If this sum is seen before, then update 
              # result with maximum
            if preSum in mp:
                res = max(res, i - mp[preSum])
    
            # Else put this sum in hash table
            else:
                mp[preSum] = i
    
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends