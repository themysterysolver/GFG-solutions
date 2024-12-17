#User function Template for python3


class Solution:
    def check(self,stalls, k, dist):
    
        # Place first cow at 0th index
        cnt = 1  
        prev = stalls[0] 
        for i in range(1, len(stalls)):
            
            # If the current stall is at least dist away
            # from the previous one place the cow here
            if stalls[i] - prev >= dist:
                prev = stalls[i] 
                cnt += 1
    
        # Return true if we are able to place all 'k' cows
        return cnt >= k

    def aggressiveCows(self,stalls, k):
      
        stalls.sort()
        res = 0 
    
        # Search Space for Binary Search
        lo = 1
        hi = stalls[-1] - stalls[0] 
    
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            # If the mid distance is possible, update
            # the result and search for larger distance
            if self.check(stalls, k, mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends