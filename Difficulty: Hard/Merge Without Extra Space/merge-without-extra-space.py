class Solution:
    def kthSmallest(self,a, b, k):
        n = len(a)
        m = len(b)
        lo = 0
        hi = n
        idx = 0
    
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = k - mid1
    
            # We don't have mid2 elements in b[], so pick more
            # elements from a[]
            if mid2 > m:
                lo = mid1 + 1
                continue
    
            # Find elements to the left and right of partition in a[]
            l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = a[mid1] if mid1 < n else float('inf')
    
            # Find elements to the left and right of partition in b[]
            l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = b[mid2] if mid2 < m else float('inf')
    
            # If it is a valid partition
            if l1 <= r2 and l2 <= r1:
                idx = mid1
                break
    
            # Check if we need to take lesser elements from a[]
            if l1 > r2:
                hi = mid1 - 1
            # Check if we need to take more elements from a[]
            else:
                lo = mid1 + 1
                
        return idx

    def mergeArrays(self,a, b):
        n = len(a)
        m = len(b)
        idx = self.kthSmallest(a, b, n)
    
        # Move all smaller elements in a[]
        for i in range(idx, n):
            a[i], b[i - idx] = b[i - idx], a[i]
    
        # Sort both a[] and b[]
        a.sort()
        b.sort()

#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends