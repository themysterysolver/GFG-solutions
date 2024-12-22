#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
        i,j=0,len(mat[0])-1
        while i<len(mat) and j>-1:
            if mat[i][j]==x:
                return True
            elif mat[i][j]>x:
                j-=1
            else:
                i+=1
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
        if ob.matSearch(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends