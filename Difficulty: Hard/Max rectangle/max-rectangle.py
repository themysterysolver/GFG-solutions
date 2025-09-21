class Solution:
    def maxArea(self, matrix):
        # code here
        def largestRectangleFromHistogram(heights):
            stack = []
            maxH = 0
            
            #finding the increasing order bars from histogram
            #stricytly increasing ones
            for i,h in enumerate(heights):
                start=i
                while stack and stack[-1][1] > h:
                    idx, ht = stack.pop()
                    maxH = max(maxH , (i-idx)*ht)
                    start = idx
                stack.append((start,h))
            
            for i,h in stack:
                maxH =  max(maxH, (len(heights)-i)*h)

            return maxH

        #--------CONVERTING MAXIMUM RECTNAGEL TO HISTOGRAM-----------
        curr = [0]*len(matrix[0])
        maxi = 0
        for row in matrix:
            for i in range(len(row)):
                if row[i]==1:
                    curr[i] += 1
                else:
                    curr[i] = 0
            maxi = max(maxi,largestRectangleFromHistogram(curr))
        return maxi