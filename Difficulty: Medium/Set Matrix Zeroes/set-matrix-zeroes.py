#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        rowZ=set()
        colZ=set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    rowZ.add(i)
                    colZ.add(j)
        for r in rowZ:
            for i in range(len(mat[0])):
                mat[r][i]=0
        for c in colZ:
            for j in range(len(mat)):
                mat[j][c]=0
                


#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends