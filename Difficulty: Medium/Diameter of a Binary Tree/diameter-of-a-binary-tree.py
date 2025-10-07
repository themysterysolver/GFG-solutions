'''
# Tree Node
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):
        # code here
        res = [0]
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            res[0] = max(res[0],l+r)
            return max(l,r)+1
        dfs(root)
        return res[0]
            
        
        
        