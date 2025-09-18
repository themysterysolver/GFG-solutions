class Solution:
    def nextGreater(self, arr):
        # code here
        nums = arr+arr
        ans = [-1]*len(nums)
        stack = []
        for i in range(len(nums)):
            if stack and nums[stack[-1]]<nums[i]:
                while stack and nums[stack[-1]]<nums[i]:
                    idx = stack.pop()
                    ans[idx] = nums[i]
            stack.append(i)
            #print(i,stack,ans)
        #print(ans)
        return ans[:len(arr)]