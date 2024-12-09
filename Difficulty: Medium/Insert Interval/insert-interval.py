#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        result = []
        newStart, newEnd = newInterval
        i = 0
    
        # Add intervals that come before the newInterval
        while i < len(intervals) and intervals[i][1] < newStart:
            result.append(intervals[i])
            i += 1
    
        # Merge overlapping intervals with newInterval
        while i < len(intervals) and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        result.append([newStart, newEnd])
    
        # Add intervals that come after the newInterval
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
    
        return result

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends