class Solution:
    def getSecondLargest(self, arr):
        # Code Herel
        l = sorted(list(set(arr)))
        #print(l)
        if len(l) <= 1:
            return -1
        else:
            return l[-2]
            