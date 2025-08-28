class Solution:
    def nextLargerElement(self,nums):
        # code here
        stack = []
        result =[-1]*len(nums)
        for i,num in enumerate(nums):
            while stack and nums[stack[-1]]<num:
                idx = stack.pop()
                result[idx] = num
            stack.append(i)
        return result