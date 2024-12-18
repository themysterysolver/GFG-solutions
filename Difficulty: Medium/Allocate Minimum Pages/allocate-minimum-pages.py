class Solution:
    
    #Function to find minimum number of pages.
    def check(self,arr, k, pageLimit):
    
        # Starting from the first student
        cnt = 1
        pageSum = 0
        for pages in arr:
            
            # If adding the current book exceeds the page 
            # limit, assign the book to the next student
            if pageSum + pages > pageLimit:
                cnt += 1
                pageSum = pages
            else:
                pageSum += pages
                
        # If books can assigned to less than k students then
        # it can be assigned to exactly k students as well
        return cnt <= k

    def findPages(self,arr, k):
        
        # If number of students are more than total books
        # then allocation is not possible
        if k > len(arr):
            return -1
        
        # Search space for Binary Search
        lo = max(arr)
        hi = sum(arr)
        res = -1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if self.check(arr, k, mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends