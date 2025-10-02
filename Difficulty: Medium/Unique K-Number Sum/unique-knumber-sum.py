class Solution:
    def combinationSum(self, n, k):
        # code here
        res = []
        def perm(idx,path):
            if len(path)>k or sum(path)>n:
                return
            if sum(path) == n and len(path) == k:
                res.append(path[:])
            else:
                for i in range(idx,10):
                    if path and path[-1] !=i:
                        perm(i,path+[i])
                    if not path:
                        perm(i,path+[i])
                
        perm(1,[])
        return res