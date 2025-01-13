
class Solution:
    def maxWater(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        res = 0
        while left < right:
            
            # Find the water stored in the container between 
            # arr[left] and arr[right]
            water = min(arr[left], arr[right]) * (right - left)
            res = max(res, water)
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return res
#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends