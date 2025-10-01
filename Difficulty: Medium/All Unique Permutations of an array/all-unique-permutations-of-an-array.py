class Solution:
    def uniquePerms(self, nums):
        vis = [False]*len(nums)
        nums.sort()
        res = []
        def perm(path):
            if len(nums) == len(path):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if vis[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not vis[i-1]:
                    continue
                vis[i] = True
                perm(path+[nums[i]])
                vis[i] = False
        perm([])
        
        return res