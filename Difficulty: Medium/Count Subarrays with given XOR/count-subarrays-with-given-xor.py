class Solution:
    def subarrayXor(self, arr, k):
        # code here
        d={0:1}
        prefixXOR=0
        result=0
        for num in arr:
            prefixXOR^=num
            if prefixXOR^k in d:
                result+=d[prefixXOR^k]
            d[prefixXOR]=d.get(prefixXOR,0)+1
        return result
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends