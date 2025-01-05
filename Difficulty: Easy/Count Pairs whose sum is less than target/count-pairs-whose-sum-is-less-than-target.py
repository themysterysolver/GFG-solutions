#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def binarySearch(self,arr, complement):
        lo, hi = 0, len(arr) - 1
        res = len(arr)
    
        while lo <= hi:
            mid = (lo + hi) // 2
    
            if arr[mid] >= complement:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
    
        return res

    def countPairs(self,arr, target):
        cnt = 0
    
        # Sort the array to use binary search
        arr.sort()
    
        for i in range(len(arr)):
            complement = target - arr[i]
    
            # Index of the element which is greater 
            # or equal to the complement
            ind = self.binarySearch(arr, complement)
    
            # arr[i] will make valid pairs with  
            # each element before the index 'ind'
            cnt += ind
    
            # If element has made a pair with itself
            if ind > i:
                cnt -= 1
    
        # Each pair is counted twice
        return cnt // 2


#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends