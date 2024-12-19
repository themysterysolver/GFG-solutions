#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        s=set(arr)
        k+=1
        for i in range(max(arr)+k):
            if i not in s:
                k-=1
                if k==0:
                    return i

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends