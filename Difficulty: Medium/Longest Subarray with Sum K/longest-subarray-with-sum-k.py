# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        mp = {}
        res = 0
        prefSum = 0
    
        for i in range(len(arr)):
            prefSum += arr[i]
    
            # Check if the entire prefix sums to k
    
            if prefSum == k:
                res = i + 1
    
            # If prefixSum - k exists in the map then there exist such 
              # subarray from (index of previous prefix + 1) to i.
            elif (prefSum - k) in mp:
                res = max(res, i - mp[prefSum - k])
    
            # Store only first occurrence index of prefSum
            if prefSum not in mp:
                mp[prefSum] = i
    
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends