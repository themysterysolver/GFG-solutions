#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        res = 0
        arr.sort()
    
        # Iterate through the array, fixing the largest side at arr[i]
        for i in range(2, len(arr)):
          
            # Initialize pointers for the two smaller sides
            left, right = 0, i - 1
    
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    # arr[left] + arr[right] satisfies the triangle inequality,
                    # so all pairs (x, right) with (left <= x < right) are valid
                    res += right - left
    
                    # Move the right pointer to check smaller pairs
                    right -= 1
                    
                else:
                    # Move the left pointer to increase the sum
                    left += 1
    
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends