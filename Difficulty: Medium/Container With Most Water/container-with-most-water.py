#two-pointer and greedy
class Solution:
    def maxWater(self, arr):
        # code here
        maxi = 0
        left,right = 0,len(arr)-1
        while left<right:
            maxi = max(maxi,min(arr[right],arr[left])*(right-left))
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
        return maxi
        