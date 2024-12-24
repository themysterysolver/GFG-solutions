
#User function Template for python3

class Solution:
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, matrix, target): 
    	# code here 
    	start,end=0,len(matrix)-1
        if len(matrix)>1:
            while start<=end:
                mid=(start+end)//2
                if matrix[mid][-1]==target:
                    return True
                elif matrix[mid][-1]<target:
                    start=mid+1
                else:
                    end=mid-1
        if start>=len(matrix) or target<matrix[start][0]:
            return False
        index=start 
        #print(index)
        start,end=0,len(matrix[index])-1
        while start<=end:
            mid=(start+end)//2
            if matrix[index][mid]==target:
                return True
            elif matrix[index][mid]<target:
                start=mid+1
            else:
                end=mid-1
        return False



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends