#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x:x[0])
        #print(intervals)
        count=0
        end=intervals[0][1]
        for x,y in intervals[1:]:
            if x<end:
                count+=1
                end=min(end,y)
            else:
                end=y
        return count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends