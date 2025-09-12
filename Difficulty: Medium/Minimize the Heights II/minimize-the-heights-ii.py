class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        ans = arr[-1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-k<0:
                continue
            minH = min(arr[0]+k,arr[i]-k)
            maxH = max(arr[-1]-k,arr[i-1]+k)
            ans = min(ans,maxH-minH)
        return ans
        