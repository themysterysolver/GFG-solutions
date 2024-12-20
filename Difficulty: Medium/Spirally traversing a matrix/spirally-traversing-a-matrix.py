class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        sol=[]
        #print(matrix)
        left=0
        top=0
        down=len(matrix)-1
        right=len(matrix[0])-1
        #print("l r t d")
        while left<=right and top<=down:
            #print(left,right,top,down)
            for i in range(left,right+1):
                sol.append(matrix[top][i])
            top+=1
            #print(left,right,top,down)
            for i in range(top,down+1):
                sol.append(matrix[i][right])
            right-=1
            #print(left,right,top,down)
            if not (left<=right and down>=top):
                break
            for i in range(right,left-1,-1):
                sol.append(matrix[down][i])
            down-=1
            #print(left,right,top,down)
            for i in range(down,top-1,-1):
                sol.append(matrix[i][left])
            left+=1
            #print(left,right,top,down)
            #print("-------------------------")
        #print(sol)
        
        return sol

#{ 
 # Driver Code Starts
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

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends