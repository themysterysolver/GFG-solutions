#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        l,h = 0 ,len(arr)-1
        while l<h:
            while arr[l] == 0 and l<h:
                l+=1
            while arr[h] == 1 and l<h:
                h-=1
            if l<h:
                arr[l],arr[h] = arr[h],arr[l]
                l+=1
                h-=1
        return arr