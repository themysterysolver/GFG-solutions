class Solution:
    def assignHole(self, mices, holes):
        # code here
        maxi = 0
        mices.sort()
        holes.sort()
        for i in range(len(mices)):
            if maxi<abs(mices[i]-holes[i]):
                maxi = abs(mices[i]-holes[i])
        return maxi
        