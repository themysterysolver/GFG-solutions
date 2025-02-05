
class Solution:
    def maxWater(self, height):
        # code here
        left=[0 for _ in range(len(height))]
        right=[0 for _ in range(len(height))]
        left_max,right_max=0,0
        for i in range(len(height)):
            left[i]=left_max
            left_max=max(height[i],left_max)
        for j in range(len(height)-1,-1,-1):
            right[j]=right_max
            right_max=max(right_max,height[j])
        #print('INDEX:',[index for index in range(len(height))])
        #print('HEIGH:',height)
        #print('LEFT :',left)
        #print('RIGHT:',right)
        total_rain_water=0
        for i in range(len(height)):
            if min(left[i],right[i])-height[i]>0:
                total_rain_water+=min(left[i],right[i])-height[i]
        return total_rain_water

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