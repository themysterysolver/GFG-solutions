#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        count=nums.count(0)
        if 0 in nums and count>=2:
            return [0]*len(nums)
        product=1
        for num in nums:
            if num==0:
                continue
            product*=num
        if count==0:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=product
                    continue
                nums[i]=product//nums[i]
            return nums
        if count==1:
            result=[0]*len(nums)
            result[nums.index(0)]=product
            return result

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends